#!/bin/bash
set -e
/usr/sbin/nginx
/usr/sbin/sshd
python3 /usr/src/app/tcpmux/tcpmux.py --listen 0.0.0.0:15 --ssh localhost:22 --tls loclhost:443 --other loclhost:443
