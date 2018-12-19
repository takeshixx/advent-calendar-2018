# XMAS QUIC

A simple server that is using the QUIC protocol.

## Building & Running

```bash
docker build -t day21_xmasquic .
docker run -d --restart=always -p 21:21/udp -v /etc/letsencrypt/archive/xmas.rip:/certs:ro --name=day21 day21_xmasquic
```

## Testing

```bash
docker build -t day21_xmasquic .
docker run -d --restart=always -p 21:21/udp -v /vagrant/.secret/certs:/certs:ro --name=day21 day21_xmasquic
```

```bash
go run client.go xmas.rip 21
```
