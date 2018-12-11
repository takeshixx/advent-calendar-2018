# .Net Remoting Service

## Building

```bash
docker build -t day10_remoting .
docker run -d --restart=always -p 10:10 --name=day10 day10_remoting
```