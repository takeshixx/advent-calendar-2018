# Websocket Service

A simple ([websocket](websocket)) Service. To solve the challenge, you need to write a short client to talk to the websocket port.

## Building & Running

```bash
docker build -t day17_websocket .
docker run -d --restart=always -p 17:17 --name=day17 day17_websocket
```

## Solution

```bash
run client.py
```
