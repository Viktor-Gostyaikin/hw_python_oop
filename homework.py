import datetime as dt


#USD_RATE = 76
#EURO_RATE = 92


class Calculator:
    records = []
    def __init__(self, limit):
       self.limit = limit
        
    def show(self): # Вывод лимита
        print(self.limit)
        
class Record:
    def __init__(self, amount, comment, date = None):  # Класс записи числа, комментария и даты.
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date  = dt.datetime.now().date().strftime('%d.%m.%y') # Порядок: module.class.def .
        else:
            self.date = date

    def show(self):
        print(f'{self.amount}, {self.date}, {self.comment}')    

r1 = Record(345, 'comment')
calc1 = Calculator(1000)
r1.show()
calc1.show()
