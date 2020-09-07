from telegram.ext import Updater


def main():
    # Создали бота и передали ему ключ для авторизации на серверах Telegram
    mybot = Updater('1332923637:AAEXSieYga231fQvQevL0Sa-BDerBidExsA', use_context=True)
    # Регулярные частые обращения за обновлениями. (Бот ходит в телегу за сообщениями)
    mybot.start_polling()
    # Бесконечный цикл бота, пока принудительно не остановишь
    mybot.idle()


main()
