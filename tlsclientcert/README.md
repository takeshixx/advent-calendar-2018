# HTTP Server with Client Cert Authentication

Access to HTTP server is only possible with a client cert with a spepcific Common Name field.

## Running

```bash
docker build -t day05_tlsclientcert .
docker run -d --restart=always -p 5:443 --name=day05 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro day05_tlsclientcert
```