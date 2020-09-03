# django-starter

##### Clear project
```bash
docker system prune
docker volume prune
docker stop $(docker ps -a -q)
docker rmi $(docker images -a -q)
docker rm $(docker ps -a -q)
docker-compose down && docker-compose build --no-cache && docker-compose up
```

##### Start the demo project
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose up
```

##### Launch project

open browser http://localhost:8000/
