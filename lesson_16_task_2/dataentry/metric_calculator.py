from datetime import date
from datetime import datetime

class MetricCalculator:
    def __init__(self):
        self.data = []
        self.sku_index = {}
        self.warehouse_index = {}
        self.operation_index = {}

    def create_index(self, column):
        if column == 'sku':
            self.sku_index = {}
            for entry in self.data:
                sku = entry.sku
                if sku not in self.sku_index:
                    self.sku_index[sku] = []
                self.sku_index[sku].append(entry)
        elif column == 'warehouse':
            self.warehouse_index = {}
            for entry in self.data:
                warehouse = entry.warehouse
                if warehouse not in self.warehouse_index:
                    self.warehouse_index[warehouse] = []
                self.warehouse_index[warehouse].append(entry)
        elif column == 'operation':
            self.operation_index = {}
            for entry in self.data:
                operation = entry.operation
                if operation not in self.operation_index:
                    self.operation_index[operation] = []
                self.operation_index[operation].append(entry)

    def calculate_profit_from_sales(self):
        total_profit = 0
        for entry in self.data:
            if entry.operation == 'sale':
                try:
                    operation_cost = float(entry.operation_cost)
                    total_profit += operation_cost
                except ValueError:
                    pass
        return total_profit

    def calculate_lost_skus(self):
        lost_skus = set()
        today = date.today()
        for entry in self.data:
            expiration_date = datetime.strptime(entry.expiration_date, "%d-%b-%Y").date()
            if expiration_date < today and entry.operation != 'sale':
                lost_skus.add(entry.sku)
        return len(lost_skus)

    def calculate_items_per_warehouse(self):
        items_per_warehouse = {}
        for entry in self.data:
            warehouse = entry.warehouse
            if warehouse not in items_per_warehouse:
                items_per_warehouse[warehouse] = 0
            items_per_warehouse[warehouse] += 1
        return items_per_warehouse

    def calculate_sold_items_per_warehouse(self):
        sold_items_per_warehouse = {}
        for entry in self.data:
            if entry.operation == 'sale':
                warehouse = entry.warehouse
                if warehouse not in sold_items_per_warehouse:
                    sold_items_per_warehouse[warehouse] = 0
                sold_items_per_warehouse[warehouse] += 1
        return sold_items_per_warehouse

    def calculate_disposed_items_per_warehouse(self):
        disposed_items_per_warehouse = {}
        for entry in self.data:
            if entry.operation == 'dispose':
                warehouse = entry.warehouse
                if warehouse not in disposed_items_per_warehouse:
                    disposed_items_per_warehouse[warehouse] = 0
                disposed_items_per_warehouse[warehouse] += 1
        return disposed_items_per_warehouse
