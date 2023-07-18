# Імпортуємо модулі.
import json
import csv
import os
from .data_entry import DataEntry

class FileProcessor:
    def __init__(self):
        """
        Клас FileProcessor.
        Ініціалізує атрибути об'єкту, які використовуються для обробки файлів і зберігання даних.
        """
        self.processed_filenames = []
        self.data = []

    def process_directory(self, directory):
        """
        Обробка всіх файлів у директорії.
        :param directory: Шлях до директорії
        """
        for filename in os.listdir(directory):
            if filename.endswith('.json') or filename.endswith('.csv'):
                file_path = os.path.join(directory, filename)
                self.process_file(file_path)
                self.processed_filenames.append(filename)

    def process_file(self, file_path):
        """
        Визначення типу файлу та виклик відповідного методу для обробки.
        :param file_path: Шлях до файлу
        """
        if file_path.endswith('.json'):
            self.process_json_file(file_path)
        elif file_path.endswith('.csv'):
            self.process_csv_file(file_path)

    def process_json_file(self, file_path):
        """
        Обробка JSON файлу.
        :param file_path: Шлях до JSON файлу
        """
        with open(file_path, 'r') as f:
            json_data = json.load(f)
            if isinstance(json_data, list):
                for record in json_data:
                    entry = DataEntry(
                        record.get('date'),
                        record.get('time'),
                        record.get('sku'),
                        record.get('warehouse'),
                        record.get('warehouse_cell_id'),
                        record.get('operation'),
                        record.get('invoice'),
                        record.get('expiration_date'),
                        record.get('operation_cost'),
                        record.get('comment')
                    )
                    self.data.append(entry)

    def process_csv_file(self, file_path):
        """
        Обробка CSV файлу.
        :param file_path: Шлях до CSV файлу
        """
        with open(file_path, 'r') as f:
            csv_reader = csv.DictReader(f)
            for record in csv_reader:
                entry = DataEntry(
                    record.get('date'),
                    record.get('time'),
                    record.get('sku'),
                    record.get('warehouse'),
                    record.get('warehouse_cell_id'),
                    record.get('operation'),
                    record.get('invoice'),
                    record.get('expiration_date'),
                    record.get('operation_cost'),
                    record.get('comment')
                )
                self.data.append(entry)
