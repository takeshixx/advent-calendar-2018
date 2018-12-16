# TLS SRP Server

A HTTP server that uses TLS-SRP. Clients can only connect with the proper username and password for the SSL/TLS session. The user is `santa` and the password is `24122018`.

## Running

```bash
docker build -t day17_tlssrp .
docker run -d --restart=always -p 17:443 -v /etc/ssl/certs:/dhparam:ro -v /etc/letsencrypt/archive/xmas.rip:/certs:ro --name=day17 day17_tlssrp
```

## Testing

```bash
docker build -t day17_tlssrp .
docker run -d --restart=always -p 17:443 -v /vagrant/.secret/dhparam:/dhparam:ro -v /vagrant/.secret/certs:/certs:ro --name=day17 day17_tlssrp
```