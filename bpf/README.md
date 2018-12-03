# eBPF Service

A simple ([eBPF](https://lwn.net/Articles/740157/)) Service which filters on a raw socket. To solve the challenge, it is needed to audit the `parse.c` file.

## Building & Running

```bash
docker build -t day09_ebpf .
docker run -d --restart=always -p 9:9 --name=day09 day09_ebpf
```

## Solution

```bash
echo "XMAS2018" | nc xmas.rip 9
```