from datetime import datetime, date

class DataEntry:
    def __init__(self, date, time, sku, warehouse, warehouse_cell_id, operation, invoice, expiration_date, operation_cost, comment):
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment

    def expired(self):
        today = date.today()
        expiration_date = datetime.strptime(self.expiration_date, "%d-%b-%Y").date()
        return expiration_date < today
