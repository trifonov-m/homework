import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

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


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    # Работа с диспетчером
    dp = mybot.dispatcher
    # Регистрация обработчика у диспетчера. Greet_user - функция, которая будет выполняться при start.
    dp.add_handler(CommandHandler("start", greet_user))
    # Добавляем обработчик сообщений, принимает только текстовые. talk_to_me - вызываемая функция
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Вывод в лог инфы о том, что бот стартовал
    logging.info("Бот стартовал")
    # Регулярные частые обращения за обновлениями. (Бот ходит в телегу за сообщениями)
    mybot.start_polling()
    # Бесконечный цикл бота, пока принудительно не остановишь
    mybot.idle()

if __name__ == '__main__':
    main()
