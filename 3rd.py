class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


payment = PaymentProcessor(CreditCardPayment())

payment.process_payment(1000)

payment.set_strategy(PayPalPayment())
payment.process_payment(2000)

payment.set_strategy(BitcoinPayment())
payment.process_payment(3000)