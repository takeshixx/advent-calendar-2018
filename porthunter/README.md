# Porthunter

## Prepare Environment

```bash
apt install nmap
```

## Deyploy Services

```bash
cp day22-porthunter.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable day22-porthunter
systemctl start day22-porthunter
```
