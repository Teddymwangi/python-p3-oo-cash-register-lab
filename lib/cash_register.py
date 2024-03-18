class CashRegister:
    def __init__(self):
        self.items = []
        self.last_transaction = 0
        self.total = 0

    def add_item(self, item_name, price, quantity=1):
        self.items.append({"item": item_name, "price": price, "quantity": quantity})
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self, discount_percentage):
        discount = self.total * discount_percentage / 100
        discount = round(discount, 2)  # Round the discount to two decimal places
        self.total -= discount
        self.total = round(self.total, 2)  # Round the total to two decimal places
        return self.total

    def void_last_transaction(self):
        if self.last_transaction != 0:
            self.total -= self.last_transaction
            self.last_transaction = 0
