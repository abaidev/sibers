## SIBERS

#### Подготовка
  - клонировать проект
  - создайте файл `.env` в корневом каталоге проекта со следующими значениями:


    SECRET_KEY=some-django-insecure-secret-key
    DEBUG=True
    DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    ALLOWED_HOSTS="127.0.0.1, localhost, 0.0.0.0"
    CSRF_TRUSTED_ORIGINS="http://localhost:8000, http://127.0.0.1:8000, http://0.0.0.0:8000"
    CORS_ORIGINS="http://localhost:8000, http://127.0.0.1:8000, http://0.0.0.0:8000"
    TIME_ZONE=Asia/Bishkek


#### Запуск проекта в виртуальной среде
для запуска проекта (без докера) вам необходимо создать виртуальную среду `python3 -m venv venv`.<br/>
активировать среду `source ./venv/bin/activate` (Ubuntu)  |   `venv\Scripts\activate` (Windows)<br/>
затем установите требования с помощью `pip install -r requirements.txt`<br/>
выполнить миграцию в БД `./manage.py migrate`<br/>
и теперь вы можете запустить проект `./manage.py runserver`. Вы можете открыть браузер по адресу [127.0.0.1:8000](http://127.0.0.1:8000/)<br/>

Все эти шаги будут выполнены автоматически, если использовать Docker.

#### Запуск проекта с Docker
  - После клонирования проекта и создания файла `.env` просто запустите команду: `docker-compose up --build`. Проект будет доступен на [0.0.0.0:8000](http://0.0.0.0:8000/)
  - Если вам нужно остановить проект: `CTRL+C`, затем можно выполнить `docker-compose down`
  - Чтобы получить доступ к bash контейнера: `docker exec -it <container_id> bash`
  - после в bash контейнера, можно создать суперпользователя, чтобы получить доступ к панели администратора `./manage.py createsuperuser`


#### Взаимодействие с веб-приложением
Проект довольно интуитивен. Вы можете увидеть ленту новостей на главной странице. Нажмите кнопку «Create News», чтобы создать новый пост. Страницы можно просматривать по 10, 20 или 50 постов на странице.