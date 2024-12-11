# Базовий клас обробника для переказів
class transfer_handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, transfer):
        # Якщо обробник не може обробити запит, передаємо його наступному обробнику
        if self.next_handler:
            self.next_handler.handle(transfer)


# Дочірній клас обробник для банківського переказу
class bank_transfer_handler(transfer_handler):
    def handle(self, transfer):
        if 100 < transfer['sum'] < 1000:
            print(f"Успішно! Виконано переказ через банківський переказ на суму: {transfer['sum']}")
        else:
            super().handle(transfer)


# Дочірній клас обробник для переказу по Western Union
class western_union_transfer_handler(transfer_handler):
    def handle(self, transfer):
        if 1000 < transfer['sum'] < 10000:
            print(f"Успішно! Виконано переказ через Western Union на суму: {transfer['sum']}")
        else:
            super().handle(transfer)


# Дочірній клас обробник для переказу по PayPal
class pay_pal_transfer_handler(transfer_handler):
    def handle(self, transfer):
        if 10000 < transfer['sum'] < 100000:
            print(f"Успішно! Виконано переказ через PayPal на суму: {transfer['sum']}")
        else:
            super().handle(transfer)


# Створення класу для системи переказів
class Transfer_System:
    def __init__(self):
        # Ланцюг передавання
        self.handler_chain = bank_transfer_handler(
            western_union_transfer_handler(
                pay_pal_transfer_handler()
            )
        )

    def make_transfer(self, sum):
        transfer = {'sum': sum}
        # Починаємо обробку переказу через ланцюг
        self.handler_chain.handle(transfer)


def enter_sum():
    sum = int(input("Введіть суму: "))
    return sum


def enter_method():
    sum = enter_sum()
    
    transfer_system = Transfer_System()
    transfer_system.make_transfer(sum)


def main():
    card_number = int(input("Введіть номер карти отримувача: "))
    while len(card_number) != 16 or card_number.isalpha():
        print("номер картки введено не вірно(недостатньо літер або присутні символи при введенні)")
        card_number = int(input("Введіть номер картки отримувача:"))
    enter_method()


if __name__ == "__main__":
    main()
