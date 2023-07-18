# Імпортуємо модулі.
import os
from .file_processor import FileProcessor
import json
from .data_entry import DataEntry

class JSONProcessor(FileProcessor):
    def process_directory(self, directory):
        """
        Обробка всіх JSON файлів у директорії.
        """
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                self.process_json_file(file_path)
                self.processed_filenames.append(filename)

    def process_json_file(self, file_path):
        """
        Обробка окремого JSON файла.
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

