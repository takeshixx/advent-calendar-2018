# TCP Images

A TCP server with a Christmas challenge-response authentication mechanism. It sends images with a random code that has to be sent back in the same TCP session to access the port.

## Running

```bash
docker build -t day19_tcpimages .
docker run -d --restart=always -p 19:19 --name=day19 day19_tcpimages
```