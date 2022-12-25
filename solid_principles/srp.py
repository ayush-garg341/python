"""
    A class should have only one job.  If a class has more than one responsibility,
    it becomes coupled.  A change to one responsibility results to modification of
    the other responsibility.
"""

print(
    "------------------------------------------  Before SRP  ---------------------------------------------"
)


class Order:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.status = "open"

    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i] * self.quantities[i]

        return total

    def pay(self, payment_type, security_code):

        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception("Unknown payment method {}".format(payment_type))


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
order.pay("debit", "09871234")


print(
    "------------------------------------------  After SRP  ---------------------------------------------"
)


class Order:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.status = "open"

    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i] * self.quantities[i]

        return total

    def set_payment_status(self):
        self.status = "paid"


class PaymentProcessor:
    def debit_pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"  # Wrong practice of setting payment status to paid, can call setStatus()

    def credit_pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_payment_status()


order = Order()
order.add_item("Peanut butter", 350, 2)
order.add_item("Muesli", 280, 1)
print(order.total_price())
payment_processor = PaymentProcessor()
payment_processor.credit_pay(order, "09871234")
print(order.status)
