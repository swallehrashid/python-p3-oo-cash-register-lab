#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        # Increase total by price * quantity
        amount = price * quantity
        self.total += amount

        # Track the last transaction amount for voiding
        self.last_transaction_amount = amount

        # Add item title to items list for each quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Apply discount: total - (total * discount / 100)
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # Subtract the last added transaction
        self.total -= self.last_transaction_amount

        # If everything is removed, total must be exactly 0.0
        if self.total < 0:
            self.total = 0.0
