#створюємо базовий клас обробник для переказів
class transfer_handler:
    def __init__(self,next_handler = None):
        self.next_handler = next_handler

    def handle(self,transfer):
        #якщо обробник не може обробити запит передаємо його настпному обробнику
        if self.next_handler:
            self.next_handler.handle(transfer)


#створюємо дочірній класс обробник для банківського переказу
class bank_transfer_handler(transfer_handler):
    def handle (self,transfer):
        if transfer['metod']=='bank':
              print(f"успішно! виконано переказ через банківський переказ на суму: {transfer['amount']}")

        else:
             super().handle(transfer)

#cтворюємо дочірній клас обробник для переказу по western-uninon 
class western_union_transter_handle(transfer_handler):
    def handle (self,transfer):
        if transfer['metod']=='Wester Union':
              print(f"успішно! виконано переказ через Western Union на суму: {transfer['amount']}")

        else:
             super().handle(transfer)

#створюємо дочірній клас обробник для переказу по Pay Pal
class pay_pal_transter_handle(transfer_handler):
    def handle (self,transfer):
        if transfer['metod']=='Pay Pal':
              print(f"успішно! виконано переказ через Western Union на суму: {transfer['amount']}")

        else:
             super().handle(transfer)

#створення класу для системи переказів
class Transfer_System:
    def __init__(self):
        #ланцюгпередання 
        self.handler_chain= bank_transfer_handler(
            western_union_transter_handle(pay_pal_transter_handle())
        )

    def make_transfer(self,amount,method):
        transfer = {'amount':amount,'metod':method}
        # Починаємо обробку переказу через ланцюг
        self.handler_chain.handle(transfer)

def enter_sum():
    sum = int(input("введіть суму: "))
    return sum


def enter_method():
    print("1.Pay Pal")
    print("2.Wester Union")
    print("3.bank")
    print("4.Exit")
    method = int(input("введіть номер системи яку бажаєте викристати: "))
    transfer_system = Transfer_System()

    if method == 1:
        sum = enter_sum()
        transfer_system.make_transfer(sum, 'Pay Pal')
    elif method == 2:
        sum = enter_sum()
        transfer_system.make_transfer(sum, 'Wester Union')
    elif method == 3:
        sum = enter_sum()
        transfer_system.make_transfer(sum, 'bank')
    elif method == 4:
        print("Exit")
        exit()
    else:
        print("wrong choice")


def main():
    card_number = int(input("введіть номер карти отримувача: "))
    enter_method()


if __name__ == "__main__":
    main()