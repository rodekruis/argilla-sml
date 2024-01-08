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
> running `docker compose down` will result in all data being lost

to make sure that argilla containers are started/stopped when the VM is started/stopped, use `docker-compose-argilla.service`.
Change `WorkingDirectory` accordingly and enable the service with
```commandline
sudo mv docker-compose-argilla.service /etc/systemd/system/
sudo systemctl enable docker-compose-argilla
```
> [!NOTE]
> when installed for the first time, argilla creates a default user `argilla` with password `1234`; make sure to delete it and create a new user, see [user management](https://docs.argilla.io/en/latest/getting_started/installation/configurations/user_management.html)

