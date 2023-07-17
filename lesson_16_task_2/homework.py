from dataentry.metric_calculator import MetricCalculator
from dataentry.file_processor import FileProcessor
from dataentry.json_processor import JSONProcessor
from dataentry.csv_processor import CSVProcessor

# Путь до папки с файлами
folder_path = r"C:\Users\arisu\PycharmProjects\learn-pyton-hillel-anna\lesson_16_task_2\SKU"

# Обработчик файлов
file_processor = FileProcessor()

# Обработка файлов в директории
file_processor.process_directory(folder_path)

# Калькулятор метрик
metric_calculator = MetricCalculator()

# Передача данных в калькулятор
metric_calculator.data = file_processor.data

# Создание индексов
metric_calculator.create_index('sku')
metric_calculator.create_index('warehouse')
metric_calculator.create_index('operation')

# Расчет метрик
total_profit = metric_calculator.calculate_profit_from_sales()
unique_lost_skus = metric_calculator.calculate_lost_skus()
items_per_warehouse = metric_calculator.calculate_items_per_warehouse()
sold_items_per_warehouse = metric_calculator.calculate_sold_items_per_warehouse()
disposed_items_per_warehouse = metric_calculator.calculate_disposed_items_per_warehouse()

# Вывод результатов
print("Total Profit:", total_profit)
print("Unique Lost SKUs:", unique_lost_skus)
print("Items per Warehouse:", items_per_warehouse)
print("Sold Items per Warehouse:", sold_items_per_warehouse)
print("Disposed Items per Warehouse:", disposed_items_per_warehouse)

# Обработка JSON-файлов
json_processor = JSONProcessor()
json_processor.process_directory(folder_path)

# Обработка CSV-файлов
csv_processor = CSVProcessor()
csv_processor.process_directory(folder_path)
