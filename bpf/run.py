#!/usr/bin/python

from __future__ import print_function
from bcc import BPF
from sys import argv

import sys
import socket
import os
import time
from scapy.all import Ether, IP, UDP, Raw
import logging
import threading
import IPython
#logging.basicConfig(filename='bpf.log',level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


current_connection = []
 

#args
def usage():
    print("USAGE: %s [-i <if_name>]" % argv[0])
    print("")
    print("Try '%s -h' for more options." % argv[0])
    exit()

#help
def help():
    print("USAGE: %s [-i <if_name>]" % argv[0])
    print("")
    print("optional arguments:")
    print("   -h                       print this help")
    print("   -i if_name               select interface if_name. Default is eth0")
    print("")
    print("examples:")
    print("    parse              # bind socket to eth0")
    print("    parse -i wlan0     # bind socket to wlan0")
    exit()

def bpf_handler():
  global current_connection

  #arguments
  interface="eth0"

  if len(argv) == 2:
    if str(argv[1]) == '-h':
      help()
    else:
      usage()

  if len(argv) == 3:
    if str(argv[1]) == '-i':
      interface = argv[2]
    else:
      usage()

  if len(argv) > 3:
    usage()

  success_text = open("./success", "rb").read()  

  print ("binding socket to '%s'" % interface)

  # initialize BPF - load source code from parse.c
  bpf = BPF(src_file = "parse.c",debug = 0)

  #load eBPF program filter of type SOCKET_FILTER into the kernel eBPF vm
  #more info about eBPF program types
  #http://man7.org/linux/man-pages/man2/bpf.2.html
  logging.info('JIT eBPF Code')
  function_filter = bpf.load_func("filter", BPF.SOCKET_FILTER)

  #create raw socket, bind it to interface
  #attach bpf program to socket created
  logging.info('Creating Raw Socket')
  BPF.attach_raw_socket(function_filter, interface)

  #get file descriptor of the socket previously created inside BPF.attach_raw_socket
  socket_fd = function_filter.sock

  #create python socket object, from the file descriptor
  sock = socket.fromfd(socket_fd,socket.PF_PACKET,socket.SOCK_RAW,socket.IPPROTO_IP)
  #set it as blocking socket
  sock.setblocking(True)

  while True:
    #retrieve raw packet from socket
    packet_str = os.read(socket_fd,2048)
    packet_bytearray = bytearray(packet_str)

    # Parse RAW data using scapy.. super general and easy
    c = Ether(packet_bytearray)
    if c.haslayer(IP):
      layer_ip = c.getlayer(IP)
      logging.info('IP: {} said the magic word ;-)'.format(layer_ip.src))
      if len(current_connection) > 0:
        for con, addr in current_connection:
          if (layer_ip.src, layer_ip.sport) == addr:
            con.send(success_text)
        logging.info('Sending success text now to: {}'.format(layer_ip.src))

def handle_client(cur, address):
  global current_connection
  data = cur.recv(2048)
  if data:
      cur.send(b"Jingle\n")
  # Lets keep the Socket short open for the other thread ;-)
  time.sleep(2)
  # Cleanup connection
  for cons, addr in current_connection:
    if address == addr:
      current_connection.remove((cons, addr))
  cur.close()


def Server():
  global current_connection
  connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  connection.bind(('0.0.0.0', 9))
  connection.listen(10)
  threads = []
  try:    
    while True:
      cur, address = connection.accept()
      current_connection.append((cur, address))
      thread = threading.Thread(target=handle_client,args=(cur,address))
      thread.start()
      threads.append(thread)

    for t in threads:
      t.join()
      
  except Exception as e:
    print("Exception: " + str(e))
    


if __name__ == "__main__":
  try:
    server_Thread = threading.Thread(target=Server)
    bpf_Thread = threading.Thread(target=bpf_handler)

    server_Thread.start()
    bpf_Thread.start()

    server_Thread.join()
    bpf_Thread.join()
  except Exception as e:
    print ("Error: unable to start thread: " + str(e))
