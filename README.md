# Ticket Support System

## Run on your local machine(development)
Clone the repo
``` shell
git clone https://github.com/mcueto/ticket_support.git
```

Get into the project folder
``` shell
cd ticket_support
```

Create a virtualenv
``` shell
mkvirtualenv tiketo
```

Set env vars(you can edit them on setenvvars.sh file)
``` shell
source setenvvars.sh
```

Install dependencies
``` shell
pip install -r requirements.txt
```

Configure your database
``` shell
docker run --name tiketo -e POSTGRES_USER=tiketo  -p 5432:5432 -d postgres:10
```

Apply migrations
``` shell
python manage.py migrate
```

Create super user(interactive)
``` shell
python manage.py createsuperuser
```

Run
``` shell
python manage.py runserver
```

Now you can visit http://127.0.0.1:8000 and log in

## Configure your database
If you have not a running postgres instance you can create a Docker container with the following code:

```bash
docker run --name tiketo -e POSTGRES_USER=tiketo  -p 5432:5432 -d postgres:10
```

This will create a PostgreSQL 10 instance based on the data contained in setenvvars.sh file
``` shell
export POSTGRES_NAME='tiketo'
export POSTGRES_USER='tiketo'
export POSTGRES_PASSWORD='tiketo'
export POSTGRES_HOST='127.0.0.1'
export POSTGRES_PORT='5432'
```
