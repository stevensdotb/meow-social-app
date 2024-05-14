# MEOW APP

### Run Project
`docker compose up --build`

### Make migration
Once the containers are running execute:<br>
`docker compose exec web python manage.py migrate`

If a model is modified, execute:<br>
`docker compose exec web python manage.py makemigrations {app_name}`


Start Playing with the app =)