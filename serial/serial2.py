import asyncore
import socket
import IPython
import random

class WriteHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock, challenge):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.chall = challenge

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class ReadHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock, challenge):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.chall = challenge

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send("FOOBAR")


class Challenge():
    # This class will force people to solve this challenge programmatically

    def __init__(self):
        self.challs_count = random.randint(2, 10) # Amount of Challenges
        self.challs = dict()
        for i in range(self.challs_count):
            self.challs[i] = self.calc_chal()
        print(self.challs)

    def calc_chal(self):
        operator_functions = {
            '+': lambda a, b: a + b, 
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b, 
            '/': lambda a, b: a / b,
        }
        operators = ["+","-","*","/"]
        operator = random.choice(operators)
        n1 = random.randint(0, 100000)
        # Avoid division by zero
        if operator == "/":
            n2 = random.randint(1, 100000)
        else:
            n2 = random.randint(0, 100000)

        result = operator_functions[operator](n1, n2)	
        return (str(n1) + str(operator) + str(n2), result)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
	asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.challenges = dict()

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
        # Splitting Handler
        if self.addr[1] == 8080:
            # Calculate Challenge
            challenge = Challenge()
            self.challenges[addr[0]] = challenge.challs
            print(self.challenges)
            print("Test")
            handler = WriteHandler(sock, challenge)
        else:
            try:
                print(self.challenges)
                challenge = self.challenges[addr[0]]
                handler = ReadHandler(sock, challenge)
            except KeyError:
                sock.send("It is SERIAL important that you do other Stuff first\n")
                sock.close()

m = multiprocessing.Manager()
challs = m.dict()
server1 = EchoServer('localhost', 8080)
server2 = EchoServer('localhost', 8081)
asyncore.loop()
