#!/usr/bin/env python3
import sys
import asyncio
import hashlib

receivers = ['rudolph', 'root', 'santa', 'alphaelve', 'lydia']


class MessageSendProtocol2:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        data = data.decode()
        print('Received %r from %s' % (data, addr))
        message = self._parse_message(data)
        if not message:
            self._send(b'Invalid message format\n', addr)
            return
        if not message['receiver'] in receivers and \
                not message['receiver'] == '*':
            self._send('-Receiver not found\n', addr)
            return
        if message['receiver_term'] and \
                message['receiver_term'] != 'console':
            self._send('-Unknown terminal ' + message['receiver_term'] + '\n', addr)
        if not self._verify_signature(addr,
                                      message['sender'],
                                      message['signature']):
            self._send('-Invalid signature ' + message['signature'] + '\n', addr)
            return
        if (message['receiver'] == 'santa' or message['receiver'] == '*') and \
                'secret' in message['message']:
            msg = '+Message delivered to Santa, have a nice XMAS!\n'
            msg += 'KNorKt0qSZPznXXGcRNRPGQYKbSclE9so0sUEBUx2GRerAJjoGA96nueapevr3hH\n'
            self._send(msg, addr)
        elif message['receiver'] == '*':
            msg = '+Message delivered to:\n'
            for r in receivers:
                msg += r + '\n'
            self._send(msg, addr)
        else:
            self._send('+Message develivered to ' + message['receiver'] + '\n', addr)

    def connection_lost(self, exc):
        pass

    def _send(self, msg, addr):
        if not isinstance(msg, bytes):
            msg = msg.encode()
        self.transport.sendto(msg, addr)
        
    def _parse_message(self, msg):
        if msg[0] != 'B':
            return False
        msg = msg[1:]
        try:
            receiver, receiver_term, message, \
                sender, sender_term, cookie, \
                signature, _ = msg.split('\x00')
        except Exception as e:
            print(e)
            return False
        ret = {
            'receiver': receiver,
            'receiver_term': receiver_term,
            'message': message,
            'sender': sender,
            'sender_term': sender_term,
            'cookie': cookie,
            'signature': signature}
        return ret

    def _verify_signature(self, addr, sender, signature):
        source_ip = addr[0]
        blake = hashlib.blake2b(digest_size=18)
        blake.update(source_ip.encode())
        blake.update(sender.encode())
        blake.update(b'XMAS2018')
        if blake.hexdigest() == signature:
            return True
        else:
            return False


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1338
    loop = asyncio.get_event_loop()
    listen = loop.create_datagram_endpoint(MessageSendProtocol2,
                                           local_addr=(host, port))
    transport, protocol = loop.run_until_complete(listen)
    print('Starting UDP listener')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    transport.close()
    loop.close()