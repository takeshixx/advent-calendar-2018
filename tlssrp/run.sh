#!/bin/bash
/usr/sbin/nginx
exec 3<> /dev/tcp/localhost/80; openssl s_server -nocert -cipher SRP -srpvfile passwd.xmas -accept 8080 -quiet <&3 >&3
