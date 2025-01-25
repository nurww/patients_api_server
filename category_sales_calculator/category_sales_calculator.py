import json
from collections import defaultdict
import logging

# Настройка логирования
logging.basicConfig(
    filename=f'category_sales_calculator.log',
    level=logging.WARNING,
    encoding='utf-8'
)

def load_data(file_path):
    # Загрузка данных из JSON-файла.
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Данные должны быть в формате списка.")
        return data
    except FileNotFoundError:
        logging.warning(f"Файл {file_path} не найден.")
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logging.warning(f"Ошибка в структуре JSON в файле {file_path}.")
        print(f"Ошибка в структуре JSON в файле {file_path}.")
        return []
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return []

def process_data(data):
    # Обработка данных: подсчет количества предметов и суммы продаж по категориям.
    # Удаляет дубликаты на основе 'id'.
    seen_ids = set()
    category_count = defaultdict(int)
    category_sales = defaultdict(int)

    for item in data:
        item_id = item.get("id")
        category = item.get("category")
        price = item.get("price")

        if item_id is None or category is None or price is None:
            logging.warning(f"Пропущена запись: {item}, некорректная структура")
            continue  # Пропускаем записи с некорректной структурой

        if item_id in seen_ids:
            logging.warning(f"Найден дубликат: {item}, пропускаем запись")
            continue  # Пропускаем дубликаты
        
        if price < 0:
            logging.warning(f"Цена отрицательная: {price}, пропускаем запись")
            continue  # Пропускаем записи с отрицательной ценой

        seen_ids.add(item_id)
        category_count[category] += 1
        category_sales[category] += price

    return dict(category_count), dict(category_sales)

def main():
    file_path = "f.json"  # Замените на путь к вашему файлу
    data = load_data(file_path)

    if not data:
        print("Нет данных для обработки.")
        logging.warning(f"Нет данных для обработки.")
        return

    category_count, category_sales = process_data(data)
    print("Количество предметов по категориям:")
    print(category_count)
    print("\nОбщая сумма продаж по категориям:")
    print(category_sales)

if __name__ == "__main__":
    main()
