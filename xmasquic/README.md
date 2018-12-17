# XMAS QUIC

A simple server that is using the QUIC protocol.

## Building & Running

```bash
docker build -t day20_xmasquic .
docker run -d --restart=always -p 20:20 --name=day20 day20_xmasquic
```

## Testing

```bash
go run client.go xmas.rip 20
```