# TLS SRP Server

A HTTP server that uses TLS-SRP. Clients can only connect with the proper username and password for the SSL/TLS session. The user is `santa` and the password is `24122018`.

## Running

```bash
docker build -t day14_tlssrp .
docker run -d --restart=always -p 14:8080 --name=day14 day14_tlssrp
```