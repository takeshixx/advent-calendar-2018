# TCP Reserved Bits

Iptables rule that drops packets where the TCP reserved bits are not set.

## Configuration

Prerequisite on the server:

```bash
sysctl -w net.ipv4.conf.all.route_localnet=1
```

Add rule:

```bash
iptables -t nat -A PREROUTING -p tcp --dport 13 -j DNAT --to 127.0.0.1:1313 -m u32 --u32 "6&0xFF=0x6 && 4&0x1FFF=0 && 0>>22&0x3C@12>>24&0x0F=0xE"
```

Remove rule:

```bash
iptables -t nat -D PREROUTING -p tcp --dport 13 -j DNAT --to 127.0.0.1:1313 -m u32 --u32 "6&0xFF=0x6 && 4&0x1FFF=0 && 0>>22&0x3C@12>>24&0x0F=0xE"
```

## Testing

Block RST from Kernel:

```bash
sudo iptables -t raw -A PREROUTING -p tcp --dport 49113 -j DROP
```

Run the test client:

```bash
sudo env/bin/python client.py 51.75.68.227 13 enp0s31f6
```

Debug on server side:

```bash
tcpdump -vvv -nn -X -i ens3 tcp port 13
```

## Running

```bash
docker build -t day13_reservedbits .
docker run -d --restart=always -p 127.0.0.1:1313:1337 --name=day13 day13_reservedbits
```

### Debugging

```bash
docker run -d --restart=always -p 127.0.0.1:1313:1337 --sysctl net.ipv4.conf.all.route_localnet=1 --cap-add=NET_ADMIN --cap-add=NET_RAW --name=day13 day13_reservedbits
```