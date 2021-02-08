import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        expense = 0
        for r in self.records:
            if r.date == today:
                expense += r.amount
            else:
                pass
        return expense

    def get_week_stats(self):
        # Расходы
        expense = 0
        # Текущая дата
        today = dt.date.today()
        # Определение конечной даты
        past_week = today - dt.timedelta(days=7)
        for r in self.records:
            if r.date >= past_week and r.date <= today:
                expense += r.amount
        return expense


class Record:
    def __init__(self, amount: float, comment: str, date=None):
        # Значение
        self.amount = amount
        # Комментарий
        self.comment = comment
        if date is None:
            self.date = dt.date.today()

        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def show(self):
        print(f'{self.amount}, {self.date}, {self.comment}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        # Дневной лимит
        limit = self.limit
        # Расходы за сегодня
        expence = self.get_today_stats()
        # Разница между лимитом и расходами
        remained = limit - expence
        if expence > limit:
            return ('Хватит есть!')
        else:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remained} кКал')


class CashCalculator(Calculator):
    USD_RATE = float(74.28)
    EURO_RATE = float(89.50)

    def get_today_cash_remained(self, currency):
        # Дневной лимит
        limit = self.limit
        # Расходы за сегодня
        expence = self.get_today_stats()
        # Разница между лимитом и расходами
        remained: float = limit - expence
        currency_name = {'eur': 'Euro', 'usd': 'USD', 'rub': 'руб'}
        ############
        if currency == 'eur':
            remained = remained / CashCalculator.EURO_RATE
        elif currency == 'usd':
            remained = remained / CashCalculator.USD_RATE
        if remained > 0:
            return (
                f"На сегодня осталось {round(remained, 2)} "
                f"{currency_name[currency]}"
            )
        elif remained == 0:
            return 'Денег нет, держись'
        else:
            return(
                f'Денег нет, держись: твой долг '
                f'- {abs(round(remained, 2))} {currency_name[currency]}'
            )


r1 = Record(345, 'comment')
r2 = Record(200, 'hehe')
c1 = CashCalculator(1000)
print(c1.get_today_cash_remained('rub'))
