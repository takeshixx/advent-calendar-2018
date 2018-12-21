#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket
from threading import Thread
from string import ascii_uppercase, digits
import time
from random import randint, choice
from multiprocessing.pool import ThreadPool
from subprocess import STDOUT, check_output, TimeoutExpired


implemented_protocols = [
    "tcp",
    "udp",
    "sctp",
]



def runner(prot, port, magic):
    cmd = {
        "tcp":["ncat", "-l"],
        "udp":["ncat", "-l", "-u"],
        "sctp":["ncat", "-l", "--sctp"],
    }
    try:
        cmd_input = cmd[prot]
        cmd_input.append("{}".format(port))
        output = check_output(cmd_input, stderr=STDOUT, timeout=30)
        if magic in str(output):
            return True
    except TimeoutExpired as e:
        if magic in str(e.output):
            return True
        else:
            return False
    return False


def on_new_client(conn,addr):
    win_condition = randint(3, 10)
    win_iter = 0
    while True:
        for i in range(0, win_condition):
            prot = choice(implemented_protocols)
            port = randint(2000, 2200)
            magic = ''.join(choice(ascii_uppercase + digits) for _ in range(10))
            msg = "protocol = {}, port = {}, magic string = {}\n".format(prot, port, magic)
            conn.send(str.encode(msg))
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(runner, (prot, port, magic))
            if(async_result.get()):
                win_iter += 1
            else:
                conn.send(b"FAILED")
                break
        
        if win_iter >= win_condition:
            # Since we used a Systemd file this needed to be a static path. 
            success = open("/home/santa/advent-calendar-2018/porthunter/success", "rb").read()
            conn.send(success)
        break
    conn.close()

if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 4444                # Reserve a port for your service.

    print('Server started!')
    print('Waiting for clients...')

    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    while True:
        c, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        thread = Thread(target = on_new_client, args = (c, addr))
        thread.start()
        thread.join()
    s.close()
