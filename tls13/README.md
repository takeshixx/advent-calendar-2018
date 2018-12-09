# HTTS Server with TLSv1.3

The HTTPS server only supports TLSv1.3.

## Building

```bash
docker build -t day12_tls13 .
docker run -d --restart=always -p 12:443 --name=day12 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day12_tls13
```