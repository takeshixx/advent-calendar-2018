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
systemctl daemon-reload
systemctl enable day03-socat
systemctl start day03-socat
```

## Testing

```bash
ncat -vv --sctp localhost 8080
```