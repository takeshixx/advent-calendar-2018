# DNS over DTLS

 A poor man's implementation of [RFC8094](https://datatracker.ietf.org/doc/rfc8094/).

 ## Running

```bash
docker build -t day20_doh .
docker run -d --restart=always -p 20:443 --cap-add=NET_ADMIN --name=day20 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day20_doh
```