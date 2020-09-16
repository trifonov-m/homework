"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    task_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Михаил', 'age': 25, 'job': 'Future Junior'}
    ]
    fields = list(task_list[0].keys())
    with open('task3.csv', 'w', encoding='utf-8') as task3:
        writer = csv.DictWriter(task3, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(task_list)


if __name__ == "__main__":
    main()
