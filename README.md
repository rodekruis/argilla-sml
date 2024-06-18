# argilla-sml
Configs and customizations of Argilla for SML

### Installation
to start argilla, run docker compose from the root directory
```commandline
sudo docker compose up -d
```
to stop argilla, run docker compose stop
```commandline
sudo docker compose stop
```
> [!WARNING]
> Running `docker compose down` will result in all data being lost

to make sure that argilla containers are started/stopped when the VM is started/stopped, use `docker-compose-argilla.service`.
Change `WorkingDirectory` accordingly and enable the service with
```commandline
sudo mv docker-compose-argilla.service /etc/systemd/system/
sudo systemctl enable docker-compose-argilla
```
> [!WARNING]
> When installed for the first time, argilla creates a default user `argilla` with password `1234`; make sure to delete it and create a new user, using `fix_users.py`.
> For more information, see [user management](https://docs.argilla.io/en/latest/getting_started/installation/configurations/user_management.html).

### Server Configuration
To ensure secure connection (HTTPS) to Argilla:
* [Install nginx](https://ubuntu.com/tutorials/install-and-configure-nginx#2-installing-nginx)
* [Port forward in nginx](https://eladnava.com/binding-nodejs-port-80-using-nginx/) 80 -> 6900
* [Install and run certbot](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04)
* Create a new domain name (myargilla.510.global) and point it to the VM's IP

To ensure that the certificate is automatically renewed

Create `/etc/systemd/system/certbot.service`
```
[Unit]
Description=Let's Encrypt renewal

[Service]
Type=oneshot
ExecStart=/usr/bin/certbot renew --quiet --agree-tos
ExecStartPost=/bin/systemctl reload nginx
```
Create `/etc/systemd/system/certbot.timer`
```
[Unit]
Description=Timer for Certbot Renewal

[Timer]
OnBootSec=300
OnUnitActiveSec=1w

[Install]
WantedBy=multi-user.target
```
Run
```commandline
systemctl enable --now certbot.timer
```
