# docker-django-skeleton

##### Start the demo project
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose up
```

##### Launch project

open browser http://localhost:8000/
