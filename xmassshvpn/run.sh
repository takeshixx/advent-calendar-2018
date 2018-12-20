#!/bin/bash
set -e
/sbin/ip link add name br0 type bridge
/sbin/ip link set br0 up
/sbin/ip tuntap add dev tap0 mode tap
/sbin/ip link set tap0 master br0
/sbin/ip link set up dev tap0
/sbin/ip tuntap add dev tap1 mode tap
/sbin/ip link set tap1 master br0
/sbin/ip link set up dev tap1
if [ ! -f /var/lib/dhcpd/dhcpd.leases ]; then
    mkdir -p /var/lib/dhcpd/
    touch /var/lib/dhcpd/dhcpd.leases
fi
/bin/chmod 755 /usr/lib
#/usr/sbin/dhcpd -cf /etc/dhcpd.conf br0
/usr/sbin/dhcpd -cf /etc/dhcpd.conf -f br0
#/usr/sbin/sshd -D -p 2222
