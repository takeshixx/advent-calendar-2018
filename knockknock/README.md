# Port Knocking

Send the magic numbers `4 8 15 16 23 42` to open the service port.

# Configuration

```bash
apt install -y knockd
cp nginx-day04.conf /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/nginx-day04.conf /etc/nginx/sites-enabled/nginx-day04.conf
service nginx restart
cp knockd.conf /etc/knockd.conf
echo 'KNOCKD_OPTS="-i ens3"' >> /etc/default/knockd
systemctl enable knockd
systemctl start knockd
```