"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as ref:
        text = ref.read()
        znaki_prepinaniya = ['.', ',', ':', '!', '?', ';']
        """
        Побаловался для удаления знаков препинания, хотя это не обязательно, т.к. они не 
        мешают подсчету слов
        """
        words_list = [x.replace(x[-1], '') if x[-1] in znaki_prepinaniya else x for x in text.split()]
        dlina = len(text)
        print(f'2. Длина получившейся строки - {dlina}')
        print(f'3. Количество слов в тексте - {len(words_list)}')
        # Замена точек в тексте на восклицательные знаки
        text_new = text.replace('.', '!')
        with open('referat2.txt', 'w', encoding='utf-8') as ref2:
            ref2.write(text_new)
        print(f'4. Результат в файле referat2.txt')


if __name__ == "__main__":
    main()
