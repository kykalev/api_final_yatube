### Описание:
Это проект ***api_final_yatube***, в котором средствами *api запросов* можно создать или просмтореть пост, написать комментарий к посту. А так же подписать на автора поста.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:kykalev/api_final_yatube.git cd api_final_yatube`

Cоздать и активировать виртуальное окружение:

`python -m venv env source env/bin/activate`

Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip pip install -r requirements.txt`

Выполнить миграции, перейдя в папку с файлом manage.py:

`python manage.py migrate`

Запустить проект:

`python3 manage.py runserver`

### Примеры запросов:

POST запрос http://127.0.0.1:8000/api/v1/posts/

`{ "text": "string", "image": "string", "group": 0 }`

POST запрос http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

`{ "text": "string" }`

POST запрос http://127.0.0.1:8000/api/v1/follow/

`{ "following": "string" }`

POST запрос http://127.0.0.1:8000/api/v1/jwt/create/

` "username": "string", "password": "string" }`

