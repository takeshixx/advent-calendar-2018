# TLS SRP Server

A HTTP server that uses TLS-SRP. Clients can only connect with the proper username and password for the SSL/TLS session. The user is `santa` and the password is `24122018`.

## Running

```bash
docker build -t day03_tlssrp .
docker run -d --restart=always -p 3:443 --name=day03 day03_tlssrp
```