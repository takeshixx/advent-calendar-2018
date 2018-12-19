#!/bin/bash
set -e
/usr/sbin/dnsmasq \
    -x /run/dnsmasq/dnsmasq.pid \
    -C /usr/src/app/dnsmasq.conf
/usr/local/bin/doh-proxy \
    --listen-address=0.0.0.0 \
    --upstream-resolver=127.0.0.1 \
    --certfile=/certs/fullchain1.pem \
    --keyfile=/certs/privkey1.pem
