#!/usr/bin/env python3
import sys
import asyncio
import random


class TcpMuxProtocl(asyncio.Protocol):
    CRLF = b'\r\n'
    SERVICES = ['santahttp',
                'echolol',
                'nfss',
                'tim3']
    MESSAGES = ['Ho ho ho',
                'It\'s christmas time, baby!']

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode().lower().strip()
        print('Data received: {!r}'.format(message))
        if message == 'help':
            for service in self.SERVICES:
                self.transport.write(service.encode())
                self.transport.write(self.CRLF)
            self.transport.close()
            return
        else:
            if message in self.SERVICES:
                self.transport.write(b'+')
            else:
                self.transport.write(b'-')
            self.transport.write(self.CRLF)
            message = random.choice(self.MESSAGES).encode()
            self.transport.write(message)
            self.transport.write(self.CRLF)


async def main():
    rv = 0
    host = '127.0.0.1'
    port = 1
    loop = asyncio.get_running_loop()
    server = await loop.create_server(
        lambda: TcpMuxProtocl(),
        host, port)
    async with server:
        print('Running server on port ' + str(port))
        try:
            await server.serve_forever()
        except Exception:
            rv = 1
    return rv


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        pass
