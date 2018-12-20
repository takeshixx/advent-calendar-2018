#!/bin/bash
set -e
/sbin/ip link add name br0 type bridge
/sbin/ip addr add 10.23.13.37/24 dev br0
/sbin/ip link set br0 up
/sbin/ip tuntap add dev tap0 mode tap
/sbin/ip link set tap0 master br0
/sbin/ip link set up dev tap0
/sbin/ip tuntap add dev tap1 mode tap
/sbin/ip link set tap1 master br0
/sbin/ip link set up dev tap1
/usr/sbin/dhcpd \
        -cf /etc/dhcpd.conf \
        -lf /usr/src/app/leases \
        br0
/usr/sbin/sshd -D -p 2222