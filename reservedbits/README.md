# TCP Reserved Bits

Iptables rule that drops packets where the TCP reserved bits are not set.

```bash
iptables -p tcp --dport 9999 -m u32 --u32 "6&0xFF=0x6 && 4&0x1FFF=0 && 0>>22&0x3C@12>>24=0x8"
```