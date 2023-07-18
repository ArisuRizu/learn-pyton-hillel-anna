# Імпортуємо модулі.
from dataentry.metric_calculator import MetricCalculator
from dataentry.file_processor import FileProcessor
from dataentry.json_processor import JSONProcessor
from dataentry.csv_processor import CSVProcessor

if __name__ == '__main__':
    # Ззаначаємо шлях до папки SKU.
    folder_path = r"C:\Users\arisu\PycharmProjects\learn-pyton-hillel-anna\lesson_16_task_2\SKU"

    # Обробник файлів.
    file_processor = FileProcessor()

    # Обробка файлів у директорії.
    file_processor.process_directory(folder_path)

    # Калькулятор метрик.
    metric_calculator = MetricCalculator()

    # Передача даних в калькулятор.
    metric_calculator.data = file_processor.data

    # Створення індексів за SKU, за складом та за операцією.
    metric_calculator.create_index('sku')
    metric_calculator.create_index('warehouse')
    metric_calculator.create_index('operation')

    # Розрахунок метрик (загального прибутку, унікальних втрачених SKU, кількості товарів за складом, кількості списаних товарів за складом.
    total_profit = metric_calculator.calculate_profit_from_sales()
    unique_lost_skus = metric_calculator.calculate_lost_skus()
    items_per_warehouse = metric_calculator.calculate_items_per_warehouse()
    sold_items_per_warehouse = metric_calculator.calculate_sold_items_per_warehouse()
    disposed_items_per_warehouse = metric_calculator.calculate_disposed_items_per_warehouse()

    # Виведення результатів.
    print("Загальний прибуток:", total_profit)
    print("Унікальні втрачені SKU:", unique_lost_skus)
    print("Товари за складом:", items_per_warehouse)
    print("Продані товари за складом:", sold_items_per_warehouse)
    print("Списані товари за складом:", disposed_items_per_warehouse)

    # Обробка JSON файлів.
    json_processor = JSONProcessor()
    json_processor.process_directory(folder_path)

    # Обробка CSV файлів.
    csv_processor = CSVProcessor()
    csv_processor.process_directory(folder_path)

