# allstar_frontend

> AllStar project

## DB Setup
```
CREATE DATABASE all_star;
CREATE ROLE django_auth WITH LOGIN PASSWORD 'asdfgh';
GRANT ALL PRIVILEGES ON DATABASE all_star TO django_auth;

python manage.py make migrations
python manage.py migrate

python manage.py createsuperuser
```
