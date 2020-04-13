# allstar_backend

> AllStar project
> Site shows vote static about football stars
> Project where you can vote for stars


## Install requirements
```
pip install -r requirements.txt
```

## DB Setup
```
CREATE DATABASE all_star;
CREATE ROLE django_auth WITH LOGIN PASSWORD 'asdfgh';
GRANT ALL PRIVILEGES ON DATABASE all_star TO django_auth;

python manage.py make migrations
python manage.py migrate

python manage.py createsuperuser
```
