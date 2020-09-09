"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    classes_list = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5a', 'scores': [3,5,5,3,4]},
        {'school_class': '6a', 'scores': [4,4,4,5,3]},
        {'school_class': '7a', 'scores': [3,3,3,5,4]}
    ]
    sum_school_mark = 0
    num_marks = 0
    for klass in classes_list:
        sum_class_scores = 0
        for mark in klass['scores']:
            sum_class_scores += mark
            klass['average_mark'] = sum_class_scores / len(klass['scores'])
        sum_school_mark += sum_class_scores
        num_marks += len(klass['scores'])
    average_school_mark = sum_school_mark / num_marks
    print(f'Средний балл по всей школе: {average_school_mark}')
    for klass in classes_list:
        print(f'Средний балл {klass["school_class"]} класса: {klass["average_mark"]}')   


if __name__ == "__main__":
    main()
