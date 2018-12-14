# Websocket Service

A simple ([websocket](websocket)) Service. To solve the challenge, you need to write a short client to talk to the websocket port.

## Building & Running

```bash
docker build -t day15_websocket .
docker run -d --restart=always -p 15:15 --name=day15 day15_websocket
```

## Solution

```bash
run client.py
```
