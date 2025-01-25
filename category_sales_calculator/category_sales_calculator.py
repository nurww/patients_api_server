import json
from collections import defaultdict
import logging

# Setting up logging
logging.basicConfig(
    filename=f'category_sales_calculator.log',
    level=logging.WARNING,
    encoding='utf-8'
)

def load_data(file_path):
    # Loading data from a JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("The data must be in list format.")
        return data
    except FileNotFoundError:
        logging.warning(f"File {file_path} not found.")
        print(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        logging.warning(f"Error in JSON structure in file {file_path}.")
        print(f"Error in JSON structure in file {file_path}.")
        return []
    except ValueError as e:
        print(f"Error in data: {e}")
        return []

def process_data(data):
    # Data processing: counting the number of items and sales by category.
    # Removes duplicates based on 'id'.
    seen_ids = set()
    category_count = defaultdict(int)
    category_sales = defaultdict(int)

    for item in data:
        item_id = item.get("id")
        category = item.get("category")
        price = item.get("price")

        if item_id is None or category is None or price is None:
            logging.warning(f"Skipped record: {item}, invalid structure")
            continue  # Skipping records with invalid structure

        if item_id in seen_ids:
            logging.warning(f"Found duplicate: {item}, skipping record")
            continue  # Skipping duplicates
        
        if price < 0:
            logging.warning(f"Price is negative: {price}, skipping record")
            continue  # Skipping records with negative price

        seen_ids.add(item_id)
        category_count[category] += 1
        category_sales[category] += price

    return dict(category_count), dict(category_sales)

def main():
    file_path = "f.json"  # Replace with your file path
    data = load_data(file_path)

    if not data:
        print("No data to process.")
        logging.warning(f"No data to process.")
        return

    category_count, category_sales = process_data(data)
    print("Number of items by category:")
    print(category_count)
    print("\nTotal sales by category:")
    print(category_sales)

if __name__ == "__main__":
    main()
