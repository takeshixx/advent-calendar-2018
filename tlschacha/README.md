# TLS ChaCha Dance

A HTTPS server that has to be accessed with specific ChaCha ciphersuite. Can be accessed e.g. with curl:

```bash
curl --ciphers DHE-RSA-CHACHA20-POLY1305 https://xmas.rip:8
```

## Building

```bash
docker build -t day08_tlschacha .
docker run -d --restart=always -p 8:443 --name=day08 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day08_tlschacha
```