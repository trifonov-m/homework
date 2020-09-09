"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import settings
import ephem

# Делаем вывод логов в bot.log
logging.basicConfig(handlers=[logging.FileHandler('bot.log', 'w', 'utf-8')], level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызван /start')
    # update.message.reply_text - ответ в чате телеграм
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

# Эхо сообщения
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_greet(update, context):
    text = 'Вызван /planet'
    print(text)
    update.message.reply_text(text)


def planet_sozv(update, context):
    user_text = update.message.text
    print(user_text)
    d = datetime.datetime.now()
    date = d
#    date = d.strftime("%Y/%m/%d")
    if user_text == 'Jupiter':
        planet = ephem.Jupiter(date) 
    update.message.reply_text(ephem.constellation(planet))
    

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    # Работа с диспетчером
    dp = mybot.dispatcher
    # Регистрация обработчика у диспетчера. Greet_user - функция, которая будет выполняться при start.
    dp.add_handler(CommandHandler("start", greet_user))
    # Добавляю команду на /planet
    dp.add_handler(CommandHandler("planet", planet_greet))
    # Добавляем обработчик сообщений, принимает только текстовые. talk_to_me - вызываемая функция
 #   dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, planet_sozv))
    # Вывод в лог инфы о том, что бот стартовал
    logging.info("Бот стартовал")
    # Регулярные частые обращения за обновлениями. (Бот ходит в телегу за сообщениями)
    mybot.start_polling()
    # Бесконечный цикл бота, пока принудительно не остановишь
    mybot.idle()

if __name__ == '__main__':
    main()
