#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket
from threading import Thread
from string import ascii_uppercase, digits
import time
from random import randint, choice
from subprocess import STDOUT, check_output, TimeoutExpired


class ClientThread(Thread): 

    implemented_protocols = [
        "tcp",
        "udp",
        "sctp",
    ]

    def __init__(self,conn,ip,port): 
        Thread.__init__(self) 
        self.conn = conn
        self.ip = ip 
        self.port = port 
        print("[+] New server socket thread started for " + ip + ":" + str(port))
 
    def run(self): 
        win_condition = randint(3, 10)
        win_iter = 0
        while True:
            for i in range(0, win_condition):
                prot = choice(self.implemented_protocols)
                port = randint(2000, 2200)
                magic = ''.join(choice(ascii_uppercase + digits) for _ in range(10))
                msg = "protocol = {}, port = {}, magic string = {}\n".format(prot, port, magic)
                self.conn.send(str.encode(msg))
                if(self.runner(prot, port, magic)):
                    win_iter += 1
                else:
                    try:
                        self.conn.send(b"FAILED")
                    except OSError:
                        pass
                    break
            
            if win_iter >= win_condition:
                # Since we used a Systemd file this needed to be a static path. 
                success = open("/home/santa/advent-calendar-2018/porthunter/success", "rb").read()
                try:
                    self.conn.send(success)
                except OSError:
                    pass
            break
        conn.close()

    def runner(self, prot, port, magic):
        cmd = {
            "tcp":["ncat", "-l"],
            "udp":["ncat", "-l", "-u"],
            "sctp":["ncat", "-l", "--sctp"],
        }
        try:
            cmd_input = cmd[prot]
            cmd_input.append("{}".format(port))
            output = check_output(cmd_input, stderr=STDOUT, timeout=4)
            if magic in str(output):
                return True
        except TimeoutExpired as e:
            if magic in str(e.output):
                return True
            else:
                return False
        return False


if __name__ == "__main__":
    TCP_IP = '0.0.0.0' 
    TCP_PORT = 22 
    
    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpServer.bind((TCP_IP, TCP_PORT)) 
    threads = [] 
    
    while True: 
        tcpServer.listen(4) 
        print("Multithreaded Python server : Waiting for connections from TCP clients...")
        (conn, (ip,port)) = tcpServer.accept() 
        newthread = ClientThread(conn,ip,port) 
        newthread.start() 
        threads.append(newthread) 
    
    for t in threads: 
        t.join() 
