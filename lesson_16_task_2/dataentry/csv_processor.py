# Імпортуємо модулі.
import os
from .file_processor import FileProcessor
import csv
from .data_entry import DataEntry

class CSVProcessor(FileProcessor):
    def process_directory(self, directory):
        """
        Обробка всіх CSV файлів у директорії.
        """
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                file_path = os.path.join(directory, filename)
                self.process_csv_file(file_path)
                self.processed_filenames.append(filename)

    def process_csv_file(self, file_path):
        """
        Обробка окремого CSV файла.
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