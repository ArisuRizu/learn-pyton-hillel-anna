# Програма для зчитування зазначеного файлу, з подальшою статистикою товару та переліком інформації про товар.
# Здійснюємо імпорт модулів для опрацювання файлу.
import csv
import os



# Функція для зчитування заланного файлу та створення індексів та словника з товаром за id.
def read_tech_inventory(filename):

    unique_id = 1
    id_index = {}
    category_index = {}
    brand_index = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:


            item = {
                'model': row['model'],
                'category': row['category'],
                'brand': row['brand'],
                'price': float(row['price'])
            }


            id_index[unique_id] = item


            category = row['category']
            if category not in category_index:
                category_index[category] = []
            category_index[category].append(unique_id)


            brand = row['brand']
            if brand not in brand_index:
                brand_index[brand] = []
            brand_index[brand].append(unique_id)

            unique_id += 1

    return id_index, category_index, brand_index



 # Функція для виведення отриманої статистики товарів з файлу за категоріями та брендами.
def print_statistics(category_index, brand_index):


    print('\nТовари за категоріями в наявності:')
    for category, items in category_index.items():
        print(f"> Категорія '{category}': {len(items)} товарів")

    print('\nТовари за брендами в наявності:')
    for brand, items in brand_index.items():
        print(f"> Бренд '{brand}': {len(items)} товарів")



 # Функція для виведення інформації про товари за обраним брендом та категорією.
def print_items_by_brand_and_category(id_index, brand_index, category_index, selected_brand, selected_category):

    items = set(brand_index.get(selected_brand, [])) & set(category_index.get(selected_category, []))

    if items:
        print(f"\nТовари бренду '{selected_brand}' у категорії '{selected_category}':")
        for item_id in items:
            item = id_index[item_id]
            print(f"ID: {item_id}, Модель: {item['model']}, Ціна: {item['price']}")
    else:
        print(f"\nНемає товарів бренду '{selected_brand}' у категорії '{selected_category}'.")

# Здійснюємо зчитування файлу, виведення статистики.
if __name__ == '__main__':
    print("\nВас вітає программа з товарами інтернет-магазину техніки.")
    print("Для успішного використання введіть бренд товару та категорію зі списку нижче!")

    current_dir = os.path.dirname(__file__)
    filename = os.path.join(current_dir, 'tech_inventory.csv')

    id_index, category_index, brand_index = read_tech_inventory(filename)

    print_statistics(category_index, brand_index)

    # Ввод товару від користувача.
    selected_brand = input("\nВведіть бренд товару, який ви шукаєте:\n> ")
    selected_category = input("\nВведіть категорію товару, яку ви шукаєте:\n> ")

    print_items_by_brand_and_category(id_index, brand_index, category_index, selected_brand, selected_category)

    print("Дякуємо, що завітали. До нових зустрічей!")