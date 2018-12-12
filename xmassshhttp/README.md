# SSH and HTTPS with TCPMUX

## Running

```bash
docker build -t day15_xmassshhttp .
docker run -d --restart=always -p 15:15 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro --name=day15 day15_xmassshhttp
```