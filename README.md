Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:kykalev/api_final_yatube.git
cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции, перейдя в папку с файлом manage.py:

python manage.py migrate

Запустить проект:

python3 manage.py runserver

Примеры запросов:

