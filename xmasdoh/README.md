# XMAS DNS over HTTPS (DoH)

 DNS Queries over HTTPS (DoH) [RFC8484](https://tools.ietf.org/html/rfc8484) port where a special TXT query has to be sent.

 ## Running

```bash
docker build -t day20_doh .
docker run -d --restart=always -p 20:443 --cap-add=NET_ADMIN --name=day20 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day20_doh
```