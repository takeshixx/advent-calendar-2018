#!/usr/bin/env python3
import sys
import io
import string
import random
import asyncio

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

images = ['Candy_stick_icon.png',
          'Christmas_candle_icon.png',
          'Santa_Claus_icon.png',
          'Snowman_icon.png',
          'Sock_icon.png']


class ImageCodeProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        self.transport = transport
        self.tries = 0
        self.code = self._gen_random_code()
        image = self._gen_random_image(self.code)
        self.transport.write(image.read())

    def data_received(self, data):
        message = data.decode().strip()
        if message != self.code:
            self.transport.write(b'Nope, sorry.\n')
            self.tries += 1
        else:
            self.transport.write(b'You got it!!\n')
            self.transport.write(b'dQfXPgFzPumJIjVvrNl86cKDiE97KHuBROn2QUu6YZn0ZClzNV3Pj86uBReQ0jSC\n')
            self.transport.close()
        if self.tries >= 3:
            self.transport.write(b'You had to many failed attempts. Come back later...\n')
            self.transport.close()

    def connection_lost(self, exc):
        self.transport.close()

    def _gen_random_code(self, n=8):
        return ''.join(random.choice(string.digits) for _ in range(n))

    def _gen_random_image(self, code):
        choice = random.choice(images)
        img = Image.open('images/' + choice)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('xmas.ttf', 100)
        draw.text((0, 100), code, (255,255,255),font=font)
        ret = io.BytesIO()
        img.save(ret, format='png')
        ret.seek(0)
        return ret

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {} host port'.format(sys.argv[0]))
        sys.exit(1)
    host = sys.argv[1]
    port = sys.argv[2]
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ImageCodeProtocol, host, port)
    server = loop.run_until_complete(coro)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
