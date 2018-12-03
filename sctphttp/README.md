# HTTP over SCTP

## Prepare Environment

```bash
apt install socat
```

## Deyploy Services

```bash
cp nginx-day03.conf /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/nginx-day03.conf /etc/nginx/sites-enabled/nginx-day03.conf
service nginx restart
cp day03-socat.service /etc/systemd/system/
cp day03-socat6.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable day03-socat
systemctl enable day03-socat6
systemctl start day03-socat
systemctl start day03-socat6
```

## Testing

```bash
ncat -v --sctp xmas.rip 3
ncat -6 -v --sctp xmas.rip 3
```