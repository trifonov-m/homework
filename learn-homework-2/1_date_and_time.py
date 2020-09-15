"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    day_today = date.today()
    delta = timedelta(days=1)
    delta30 = timedelta(days=30)
    day_yesterday = (day_today - delta)
    day_tomorrow = day_today + delta
    day_30back = day_today - delta30
    print(f"Вчера: {day_yesterday.strftime('%A %d %B %Y')}")
    print(f"Сегодня: {day_today.strftime('%A %d %B %Y')}")
    print(f"30 дней назад: {day_30back.strftime('%A %d %B %Y')}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    print(date_dt)


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
