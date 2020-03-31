# allstar_backend

> AllStar project. Users can registrations on site and login in system for vote. There user can see some statistics about football stars.


## Install requirements
```
pip install -r requirements.txt
```

## DB Setup
```
CREATE DATABASE all_star;
CREATE ROLE django_auth WITH LOGIN PASSWORD 'asdfgh';
GRANT ALL PRIVILEGES ON DATABASE all_star TO django_auth;

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```
