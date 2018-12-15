from __future__ import print_function
from keystone import *
from unicorn import *
from unicorn.x86_const import *
import array
import random
import socket
import sys
from thread import start_new_thread

HOST = '' # all availabe interfaces
PORT = 16 # arbitrary non privileged port 

def emulate(emulation_code):
	ADDRESS = 0x1000000
	#print("Emulate i386 code")
	# Initialize emulator in X86-32bit mode
	mu = Uc(UC_ARCH_X86, UC_MODE_32)
	# map 1MB memory for this emulation
	mu.mem_map(ADDRESS, 2 * 1024 * 1024)
	mu.mem_write(ADDRESS, emulation_code)
	# emulate code in infinite time & unlimited instructions
	mu.emu_start(ADDRESS, ADDRESS + len(emulation_code))
	r_eax = mu.reg_read(UC_X86_REG_EAX)
	print(">>> EAX = 0x%x" %r_eax)
	return r_eax
	

def generate():
	# separate assembly instructions by ; or \n
	CODE = b"XOR EAX,EAX;"
 
	mnemonics = [
		b"INC eax;",
		b"DEC eax;",
		b"MOV eax, {0};",
		b"SHR eax, {0};",
		b"SHL eax, {0};",
		b"SAR eax, {0};",
		b"SAL eax, {0};",
		b"RCR eax, {0};",
		b"RCL eax, {0};",
		b"ADD eax, {0};",
		b"SUB eax, {0};",
	]

	#len_instructions = randint(4, 15)
	for _ in range(0, random.randint(4,15)):
		choice = random.choice(mnemonics)
		if "{0}" in choice:
			choice = choice.format(random.randint(0, 100))
		CODE += choice
	return CODE

def check_answer(answer, result):
    if not answer:
        return False
    try:
        if answer.startswith("0x"):
            answer = int(data, 16)
        if int(answer) == result:
            return True
        else:
            return False
    except ValueError:
        return False
    return False

def client_thread(conn):
    conn.send("Welcome to Santas Unicorn... uhmmm Reindeer Server. This is a binary challenge ;-).\n")
    try:
    	# Initialize engine in X86-32bit mode
        CODE = generate()
        CODE2 = generate()
        ks = Ks(KS_ARCH_X86, KS_MODE_32)
        encoding, count = ks.asm(CODE)
        encoding2, count2 = ks.asm(CODE2)
	#print("%s = %s (number of statements: %u)" %(CODE, encoding, count))
        instructions = array.array('B', encoding).tostring()
        instructions2 = array.array('B', encoding2).tostring()
        result = emulate(instructions)
        result2 = emulate(instructions2)
        print(result)
        print(result2)
    except KsError as e:
        print(CODE)
        print("ERROR: %s" %e)
        conn.send("Something went horribly wrong on our side :( please connect again")

    conn.send("Your first Challenge is>")
    conn.send(instructions)
    conn.send("\n\n\nYour Answer for EAX?:\n")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if check_answer(data, result):
            reply = "Wow your first challenge was correct ;-) just to be sure you had no luck lets try another one\n"
            conn.sendall(reply)
            conn.send("Your second challenge is>")
            conn.send(instructions2)
            conn.send("\n\n\nYour Answer for EAX?:\n")
                
            data = conn.recv(1024)
            if not data:
                break
            if check_answer(data, result2):
                success = open("./success", "rb").read()
                conn.sendall(success)
                break
        else:
            conn.sendall("WRONG\n")
            break
    conn.close()



if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
        sys.exit(0)

    print("[-] Socket Created")

# bind socket
    try:
        s.bind((HOST, PORT))
        print("[-] Socket Bound to port " + str(PORT))
    except socket.error as msg:
        print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
        sys.exit()
    s.listen(10)
    print("Listening...")
    while True:
        # blocking call, waits to accept a connection
        conn, addr = s.accept()
        print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

        start_new_thread(client_thread, (conn,))
    s.close()
