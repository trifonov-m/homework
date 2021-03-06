"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    q_a_dict = {
      "Как дела?": "Хорошо!",
      "Что делаешь?": "Программирую",
      "Нравится Python?": "print('Да')"
    }
    a = input('Введите вопрос. Пожалуйста, заканчивайте вопрос вопросительным знаком. Вопрос: ')
    while True:
        try:
            if a in q_a_dict.keys():
                print(q_a_dict[a])
            else:
                print('Неизвестный вопрос. Задайте другой ')
            a = input('Введите вопрос. Пожалуйста, заканчивайте вопрос вопросительным знаком. Вопрос: ')
        except KeyboardInterrupt:
            print('Вопросы закончились. Пока!')
            break
    
if __name__ == "__main__":
    ask_user()
