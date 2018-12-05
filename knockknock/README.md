# Port Knocking

Send the magic numbers `42 23 16 15 8` to open the service port.

## Configuration

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

## Testing

```bash
ncat xmas.rip 42
ncat xmas.rip 23
ncat xmas.rip 16
ncat xmas.rip 15
ncat xmas.rip 8
curl xmas.rip:4
```