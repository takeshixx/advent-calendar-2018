#!/usr/bin/env python3
import sys
import asyncio
import hashlib


class MessageSendProtocol2:
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {} host port'.format(sys.argv[0]))
        sys.exit(1)
    host = sys.argv[1]
    port = sys.argv[2]
    loop = asyncio.get_event_loop()
    message = "B"
    message += "santa\x00" # receiver
    message += "\x00" # receiver_term
    message += "Hello my friend, gimme secret\x00" # message
    message += "sandy\x00" # sender
    message += "console\x00" # sender_term
    message += "910806121325\x00" # cookie
    blake = hashlib.blake2b(digest_size=18)
    blake.update(b'127.0.0.1')
    blake.update(b'sandy')
    blake.update(b'XMAS2018')
    message += blake.hexdigest()
    message += '\x00'
    connect = loop.create_datagram_endpoint(
        lambda: MessageSendProtocol2(message, loop),
        remote_addr=(host, port))
    transport, protocol = loop.run_until_complete(connect)
    loop.run_forever()
    transport.close()
    loop.close()
