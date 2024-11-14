#створюємо базовий клас обробник для переказів
class transfer_handler:
    def __init__(self,next_handler = None):
        self.next_handler = next_handler

    def handle(self,transfer):
        #якщо обробник не може обробити запит передаємо його настпному обробнику
        if self.next_handler:
            self.next_handler.handle(transfer)



