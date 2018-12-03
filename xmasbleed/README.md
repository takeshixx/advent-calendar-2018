# XMASbleed

A slightly modified OpenSSL 1.0.1f which is vulnerable to heartbleed. But instead of leaking actual memory, it leaks christmas fun!

## Building

```bash
git clone git@github.com:openssl/openssl.git
cd openssl
git checkout OpenSSL_1_0_1f
git apply openssl101f_xmasbleed.patch
./config
make -j4
```

After building the libraries, build the command line utility for testing:

```bash
cd apps
make -j4
```

## Testing

After building the command line utility it can be used to run a testing server:

```bash
cd openssl/apps
./openssl s_server
```

Can then be exploited with [hb-test.py](https://gist.github.com/takeshixx/10107280):

```bash
python2 hb-test.py -p 4433 localhost
```

And dump all memory into a file (e.g. if we switch to ASCII arts):

```bash
python2 hb-test.py -p 4433 -f /tmp/xmasbleed localhost
```

## Running

```bash
docker build -t day02_xmasbleed .
docker run -d --restart=always -p 2:443 --name=day02 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day02_xmasbleed
```