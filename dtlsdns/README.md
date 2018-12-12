# DNS over DTLS

 A poor man's implementation of [RFC8094](https://datatracker.ietf.org/doc/rfc8094/).

 ## Running

```bash
docker build -t day14_dtlsdns .
docker run -d --restart=always -p 14:5353 --name=day14 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day14_dtlsdns
```