# Marketplace Backend

Минимальный backend для marketplace на Django REST Framework.

## Стек

- Django
- Django REST Framework
- JWT авторизация
- PostgreSQL
- Redis
- Docker
- Swagger / OpenAPI

## Что реализовано

- Каталог товаров
- Карточка товара
- Регистрация и логин
- JWT access и refresh токены
- Корзина пользователя
- Минимальный личный кабинет со списком покупок
- Минимальная админка товаров: добавить, изменить, удалить

## Установка без Docker

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Создать файл `.env` по примеру `.env.example`.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск через Docker

```bash
docker compose up --build
```

Backend будет доступен по адресу:

```text
http://localhost:8000/
```

Создать администратора:

```bash
docker compose exec web python manage.py createsuperuser
```

Остановить контейнеры:

```bash
docker compose down
```

Остановить контейнеры и удалить данные PostgreSQL:

```bash
docker compose down -v
```

## Переменные окружения

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

POSTGRES_DB=marketplace
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_URL=redis://127.0.0.1:6379/1
```

Для Docker `POSTGRES_HOST` и `REDIS_URL` переопределяются в `docker-compose.yml`.

## Swagger

Swagger доступен по адресу:

```text
http://localhost:8000/swagger/
```

OpenAPI schema:

```text
http://localhost:8000/schema/
```

## Endpoints

Base URL:

```text
http://localhost:8000
```

Auth:

```text
POST /users/register/
POST /users/login/
POST /users/token/refresh/
GET  /users/me/
```

Products:

```text
GET    /products/
GET    /products/<id>/
POST   /products/product/
PUT    /products/product/<id>/
DELETE /products/product/<id>/
```

Cart:

```text
GET    /cart/
POST   /cart/add/
DELETE /cart/remove/<product_id>/
```

Orders:

```text
GET /orders/
```

Для защищённых запросов нужен заголовок:

```text
Authorization: Bearer <access_token>
```
