# Message Send Protocol 2 (RFC1312)

A Python implementation of the Message Send Protocol [RC1312](https://tools.ietf.org/html/rfc1312) with an insanely secure signature verification.

## Running

```bash
docker build -t day18_msp2 .
docker run -d --restart=always -p 18:1338 --name=day18 day18_msp2
```