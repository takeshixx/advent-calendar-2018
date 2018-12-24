# Merry Xmas

Just some trolling for Christmas Eve.

## Running

```bash
docker build -t day24_merryxmas .
docker run -d --restart=always -p 24:443 --name=day24 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day24_merryxmas
```