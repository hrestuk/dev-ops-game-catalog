# Game Catalog

Вебзастосунок на Django для перегляду каталогу комп'ютерних ігор.

## Можливості

- Головна сторінка сайту.
- Каталог комп'ютерних ігор.
- Збереження інформації про ігри в базі даних SQLite.
- Адміністративна панель Django для керування іграми.
- Автоматизовані модульні тести.
- Контейнеризація за допомогою Docker.
- CI/CD через GitHub Actions із публікацією Docker-образу в Docker Hub.

## Технології

- Python 3.12
- Django
- SQLite
- Git та GitHub
- Docker
- GitHub Actions
- Docker Hub

## Запуск локально

Встановити залежності:

```bash
python -m pip install -r requirements.txt
```

Застосувати міграції бази даних:

```bash
python manage.py migrate
```

Запустити вебсервер:

```bash
python manage.py runserver
```

Відкрити сайт: http://127.0.0.1:8000/

## Адміністративна панель

Створити адміністратора:

```bash
python manage.py createsuperuser
```

Відкрити адміністративну панель: http://127.0.0.1:8000/admin/

## Запуск тестів

```bash
python manage.py test
```

## Запуск через Docker

Завантажити образ із Docker Hub:

```bash
docker pull hrestuk/game-catalog:latest
```

Запустити контейнер:

```bash
docker run --rm -p 8000:8000 hrestuk/game-catalog:latest
```

Відкрити сайт: http://127.0.0.1:8000/

## CI/CD

GitHub Actions автоматично запускає перевірку конфігурації Django та модульні тести після push у гілку `master`.

Якщо тести успішні, GitHub Actions збирає Docker-образ і публікує його в Docker Hub.

Репозиторій Docker Hub: https://hub.docker.com/r/hrestuk/game-catalog

## Автор

Навчальний проєкт для практичної роботи №4 з веброзробки та DevOps.
