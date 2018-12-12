# SSH and HTTPS with TCPMUX

A TCP multiplexer port that runs HTTPS and SSH. HTTPS will give a hint about SSH, secret is only available via SSH. Login with *santa*:*santa*.

## Running

```bash
docker build -t day15_xmassshhttp .
docker run -d --restart=always -p 15:15 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro --name=day15 day15_xmassshhttp
```