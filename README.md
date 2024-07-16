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
> When installed for the first time, argilla creates a default user `argilla` with password `1234`; make sure to delete it and create a new user, using `fix_users.py`. After doing this, uncomment the line in `docker-compose.yaml` containing `DEFAULT_USER_ENABLED: false`, otherwise `docker compose up -d` will fail when the VM reboots.
> For more information, see [user management](https://docs.argilla.io/en/latest/getting_started/installation/configurations/user_management.html).

### Server Configuration
To ensure secure connection (SSL) to Argilla:

#### 1. Install and configure nginx
Install nginx
```commandline
sudo apt update
sudo apt install nginx
```
Run
```commandline
sudo rm /etc/nginx/sites-enabled/default
```
Create `/etc/nginx/sites-available/sml`
```
server {
    server_name my.argilla.url.com;

    location / {
        proxy_set_header   X-Forwarded-For $remote_addr;
        proxy_set_header   Host $http_host;
        proxy_pass         "http://127.0.0.1:6900";
    }
}
```
Run
```commandline
sudo ln -s /etc/nginx/sites-available/sml /etc/nginx/sites-enabled/sml
sudo service nginx restart
```
#### 2. Install certbot
[Install and run certbot](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04). This will also take care of renewing the certificate.
#### 3. Set up domain name
Create a new domain name (`my.argilla.url.com`) and point it to the VM's IP
