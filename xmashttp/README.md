# XMAS HTTP Server

A HTTP server with a special **XMAS** method.

## Running

```bash
docker build -t day07_xmashttp .
docker run -d --restart=always -p 7:80 --name=day07 day07_xmashttp
```