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
              print(f"Переказ через банківський переказ на суму: {transfer['amount']}")

        else:
             super().handle(transfer)

#cтворюємо дочірній клас обробник для переказу по western-uninon 
class western_union_transter_handle(transfer_handler):
    def handle (self,transfer):
        if transfer['metod']=='westerUnion':
              print(f"Переказ через Western Union на суму: {transfer['amount']}")

        else:
             super().handle(transfer)

#створюємо дочірній клас обробник для переказу по Pay Pal
class pay_pal_transter_handle(transfer_handler):
    def handle (self,transfer):
        if transfer['metod']=='payPal':
              print(f"Переказ через Western Union на суму: {transfer['amount']}")

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
        transfer = {'amount':amount,'method':method}
        # Починаємо обробку переказу через ланцюг
        self.handler_chain.handle(transfer)


