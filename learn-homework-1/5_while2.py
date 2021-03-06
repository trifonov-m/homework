"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user_dict():
    """
    Замените pass на ваш код
    """
    # немного странное название переменной - не говорящее
    # я бы назвала что то вроде answers_dict 
    answers_dict = {
      "Как дела?": "Хорошо!",
      "Что делаешь?": "Программирую",
      "Нравится Python?": "print('Да')"
    }
    a = input('Введите вопрос. Пожалуйста, заканчивайте вопрос вопросительным знаком. Вопрос: ')
    while a[-1] == '?':
      # 4 строчки ниже можно записать в одну с помощью оператора get()
      # q_a_dict.get(a, 'Неизвестный вопрос. Задайте другой ')
#        if a in answers_dict.keys():
#            print(answers_dict[a])
#        else:
#            print('Неизвестный вопрос. Задайте другой ')
        print(answers_dict.get(a, 'Неизвестный вопрос. Задайте другой '))
        a = input('Введите вопрос. Пожалуйста, заканчивайте вопрос вопросительным знаком. Вопрос: ')
    print('Вопросы закончились. Пока!')
    
if __name__ == "__main__":
    ask_user_dict()
