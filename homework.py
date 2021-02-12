'''Два калькулятора: для подсчёта денег(CashCalculator) и
калорий(CaloriesCalculator)'''
import datetime as dt


class Calculator:
    '''Родительский класс калькуляторов. Принмает аргумент limit.
    В конструкторе создан пустой список, в котором потом
    будут храниться записи.
    add_record сохраняет в список запись.
    get_today_stats показывает сколько потрачено/съедено сегодня.
    get_week_stats показывает сколько потрачено/съедено за прошедшую неделю
    get_remained показывает разницу значений между limit и get_today_stats'''

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self):
        today = dt.date.today()
        date_week_ago = today - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                   if date_week_ago < record.date <= today)

    def get_remained(self):
        remained = self.limit - self.get_today_stats()
        return remained


class Record:
    '''Класс записей. Принимает аргументы: значение, комментарий, дата.
    Если дата не указывается пользователем, то подставляется текущая дата'''
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()

        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def __str__(self):
        return f'Record({self.amount}, {self.date}, {self.comment})'


class CaloriesCalculator(Calculator):
    '''Класс калькулятора калорий наследующий класс Calculator.
    Метод get_calories_remained определяет, сколько ещё калорий можно/нужно
    получить сегодня'''
    def get_calories_remained(self):
        if self.get_remained() <= 0:
            return 'Хватит есть!'
        return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                f'калорийностью не более {self.get_remained()} кКал')


class CashCalculator(Calculator):
    '''Класс калькулятора денег наследующий класс Calculator.
        Метод get_today_cash_remained определяет, сколько ещё денег
можно потратить сегодня в рублях, долларах или евро'''
    USD_RATE = 72.12
    EURO_RATE = 85.21
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        remained = self.get_remained()
        currency_dir = {
            'eur': ('Euro', self.EURO_RATE,),
            'usd': ('USD', self.USD_RATE,),
            'rub': ('руб', self.RUB_RATE,)
        }
        currency_name, currency_rate = currency_dir[currency]
        list_of_currency = list(currency_dir.keys())
        debt_1 = remained / currency_rate
        debt_2 = abs(round(debt_1, 2))
        if self.get_remained() == 0:
            return 'Денег нет, держись'
        if currency not in currency_dir:
            return f'Валюта неверная, правильные: {list_of_currency}'
        if self.get_remained() < 0:
            return(
                'Денег нет, держись: твой долг '
                f'- {debt_2} {currency_name}'
            )
        return ('На сегодня осталось '
                f'{debt_2} {currency_name}')
