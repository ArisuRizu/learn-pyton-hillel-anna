# Імпортуємо модуль.
from datetime import datetime, date

class DataEntry:
    def __init__(self, date, time, sku, warehouse, warehouse_cell_id, operation, invoice, expiration_date, operation_cost, comment):
        """
        Клас DataEntry.
        Ініціалізує атрибути об'єкту, які представляють поля запису даних.
        :param date: Дата
        :param time: Час
        :param sku: SKU
        :param warehouse: Склад
        :param warehouse_cell_id: ID комірки складу
        :param operation: Операція
        :param invoice: Рахунок
        :param expiration_date: Дата закінчення терміну придатності
        :param operation_cost: Вартість операції
        :param comment: Коментар
        """
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
        """
        Перевірка, чи товар має закінчений термін придатності.
        :return: True, якщо товар має закінчений термін придатності; False - у іншому випадку
        """
        today = date.today()
        expiration_date = datetime.strptime(self.expiration_date, "%d-%b-%Y").date()
        return expiration_date < today
