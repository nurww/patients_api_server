# Patients API Server

## Описание
API-сервер для управления пациентами. Реализованы два эндпоинта:
- `/login`: Получение JWT-токена.
- `/patients`: Получение списка пациентов (доступно только для докторов).

## Структура проекта
- `app/`: Исходный код.
- `tests/`: Тесты.
- `migrations/`: Миграции базы данных.
- `requirements.txt`: Зависимости проекта.

## Установка и запуск
1. Установите зависимости:
   pip install -r requirements.txt
2. Выполните миграции базы данных:
   alembic upgrade head
3. Запустите сервер:
   uvicorn app.main:app --reload
4. Приложение будет доступно по адресу: http://localhost:8000.

## Запуск с использованием Docker
1. Проверьте установку Docker: Убедитесь, что Docker установлен и работает:
   docker --version
2. Создайте Docker-образ: Соберите образ приложения:
   docker build -t patients-api .
3. Запустите контейнер: Выполните команду:
   docker run -d -p 8000:8000 patients-api
4. Приложение будет доступно по адресу: http://localhost:8000.

## Примеры запросов
### /login
   #### Запрос:
   ```
   curl -X POST http://localhost:8000/login \
   -H "Content-Type: application/json" \
   -d '{"username": "doctor", "password": "pass"}'
   ```
   #### Ответ:
   ```
   {
      "access_token": "eyJhbGciOiJIUzI1...",
      "token_type": "bearer"
   }
   ```

### /patients
   #### Запрос:
   ```
   curl -X GET http://localhost:8000/patients \
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   ```
   #### Ответ:
   ```
   [
      {
         "id": 1,
         "date_of_birth": "1980-01-01",
         "diagnoses": ["Diabetes"],
         "created_at": "2023-01-01T12:00:00"
      },
      ...
   ]
   ```

## Тесты
### Для запуска тестов используйте:
   ```
   pytest --cov=app tests/
   ```
### Покрытие тестами: Отчёт о покрытии будет отображён после завершения тестов.

## Настройка `alembic.ini`
Для корректной работы миграций с Alembic, убедитесь, что в файле `alembic.ini` в секции `[alembic]` используется строка подключения к базе данных:

```ini
sqlalchemy.url = mysql+pymysql://root:root@localhost/mad_devs
```

## Настройка `migrations/env.py`
Файл `migrations/env.py` использует вашу модель базы данных. Чтобы это работало, строка в `env.py` должна выглядеть так:

```ini
from app.models import Base

target_metadata = Base.metadata
```

# Category Sales Calculator

## Usage

### Navigate to the `category_sales_calculator` directory:
```
cd category_sales_calculator
```

### Place a JSON file with sales data in this directory. The file must adhere to the following format:
```
[
  {
    "id": 1,
    "owner": "user2",
    "price": 8647,
    "category": "cat1"
  },
  ...
]
```
### Run the calculator:
```
python category_sales_calculator.py
```
### The output will display the number of items and total sales per category:
```
Количество предметов по категориям:
{'cat1': 333103, 'cat3': 333386, 'cat2': 333511}

Общая сумма продаж по категориям:
{'cat1': 1831348772, 'cat3': 1832844186, 'cat2': 1832867646}
```