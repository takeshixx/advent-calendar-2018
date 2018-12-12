#!/bin/bash
set -e
/usr/sbin/nginx
/usr/sbin/sshd
/usr/bin/python3 /usr/src/app/tcpmux/tcpmux.py --listen 0.0.0.0:15 --ssh 127.0.0.1:22 --tls 127.0.0.1:443 --other 127.0.0.1:443
