# DHCP via SSH

The challenge is to send DHCP requests to the host via a SSH layer 2 VPN.

## Running

```bash
docker build -t day23_xmassshvpn .
docker run -d --restart=always -p 23:22 --cap-add=NET_ADMIN --cap-add=NET_RAW --name=day23 day23_xmassshvpn
```