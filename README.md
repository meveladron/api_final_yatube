API для социальной сети YaTube - https://github.com/meveladron/hw05_final.

Yatube - Это социальная сеть для блогеров. Данный проект реализован на языке
Python с применением фреймворка Django. В качестве базы данных используется SQLite.
Социальная сеть поддерживает создание постов для каждого пользователя, а также подписки
на других авторов и комментирование постов.

Позволяет делать запросы к моделям проекта: Посты, Группы, Комментарии, Подписки.
Поддерживает методы GET, POST, PUT, PATCH, DELETE
Предоставляет данные в формате JSON

### Технологии:
- Python 3.9.1
- Django REST Framework 3.12.4
- Django 3.2.16
- Djangorestframework-simplejwt 4.7.2
- PyJWT 2.1.0
- Pillow 9.3.0


### Установка проекта:

Клонировать репозиторий и перейти в через терминал:

```
git clone git@github.com:meveladron/api_final_yatube.git
```

```
cd api_yatube
```

Cоздать виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:

```
source venv/bin/activate
```

Установить и обновить пакетный менеджер pip:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
