import datetime as dt


class Calculator:
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
        limit = self.limit
        expence = self.get_today_stats()
        remained = limit - expence
        return remained


class Record:
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
    def get_calories_remained(self):
        if self.get_today_stats() >= self.limit:
            return 'Хватит есть!'
        if self.get_today_stats() < self.limit:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {self.get_remained()} кКал')


class CashCalculator(Calculator):
    USD_RATE = 72.12
    EURO_RATE = 85.21

    def get_today_cash_remained(self, currency):
        remained = self.get_remained()
        currency_dir = {
            'eur': ['Euro', self.EURO_RATE],
            'usd': ['USD', self.USD_RATE],
            'rub': ['руб', 1]
        }
        list_of_currency = list(currency_dir.keys())
        debt_1 = remained / currency_dir[currency][1]
        debt_2 = abs(round(debt_1, 2))
        cur = currency_dir[currency][0]
        if currency not in currency_dir:
            return f'Валюта неверная, правильные: {list_of_currency}'
        if self.get_today_stats() == self.limit:
            return 'Денег нет, держись'

        if self.get_today_stats() > self.limit:
            return(
                'Денег нет, держись: твой долг '
                f'- {debt_2} {cur}'
            )
        if self.get_today_stats() < self.limit:
            return ('На сегодня осталось '
                    f'{debt_2} {cur}')
