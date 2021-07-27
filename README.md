# Django starter

##### Clear

```bash
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```

##### Dev

```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose run web python3 manage.py loaddata initial_data
docker-compose up
```

##### Production

```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml run web python3 manage.py makemigrations
docker-compose -f docker-compose.prod.yml run web python3 manage.py migrate
docker-compose -f docker-compose.prod.yml run web python3 manage.py createsuperuser
docker-compose -f docker-compose.prod.yml run web python3 manage.py loaddata initial_data
docker-compose -f docker-compose.prod.yml up -d
```
