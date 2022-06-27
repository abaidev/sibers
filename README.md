## SIBERS

#### Preparations
  - clone project
  - create .env file in root directory of the proj with following values:


    SECRET_KEY=some-django-insecure-secret-key
    DEBUG=True
    DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    ALLOWED_HOSTS="127.0.0.1, localhost, 0.0.0.0"
    CSRF_TRUSTED_ORIGINS="http://localhost:8000, http://127.0.0.1:8000, http://0.0.0.0:8000"
    CORS_ORIGINS="http://localhost:8000, http://127.0.0.1:8000, http://0.0.0.0:8000"
    TIME_ZONE=Asia/Bishkek


#### Running project in virtual environment
to run project (without docker) you need to create virtual environment `python3 -m venv venv`.<br/>
activate environment `source ./venv/bin/activate` (Ubuntu) `venv\Scripts\activate` (Windows)<br/>
then install requirements by `pip install -r requirements.txt`<br/>
make migrations to DB `./manage.py migrate`<br/>
and now you can run project `./manage.py runserver`. You can open browser on [127.0.0.1:8000](http://127.0.0.1:8000/)<br/>

All these steps are could be managed behind the scenes if use Docker. 

#### Running project with Docker
  - After clone project and create `.env` file, just run command: `docker-compose up --build`. Project will be [0.0.0.0:8000](http://0.0.0.0:8000/)
  - If you need stop project: `CTRL+C`, and `docker-compose down` to stop and remove containers and networks
  - To access container bash: `docker exec -it <container_id> bash`
  - and create superuser in container bash to get access to admin panel `./manage.py createsuperuser`


#### Interactions with webapp
Project pretty intuitive. You can see news feed on home page. Press `Create News` button to create new post. Paginate pages by 10, 20 or 50 posts per page.