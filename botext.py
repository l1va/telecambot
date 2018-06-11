import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

TOKEN = 'YOUR_TOKEN'
REQUEST_KWARGS = {
    # 'proxy_url': 'http://91.198.137.114:3128',
    # Optional, if you need authentication:
    # 'urllib3_proxy_kwargs': {
    #     'username': 'PROXY_USER',
    #     'password': 'PROXY_PASS',
    # }
}


def run_bot():
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I'm a super bot, i know /webcam command!")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    def echo(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="use commands with slash(/) please")  # update.message.text)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    def webcam(bot, update):
        bot.send_photo(chat_id=update.message.chat_id, photo=open('img.png', 'rb'))

    webcam_handler = CommandHandler('webcam', webcam)
    dispatcher.add_handler(webcam_handler)

    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="sorry, I understand only /webcam command.")

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
    updater.stop()
    print("telegram bot done")


if __name__ == "__main__":
    run_bot()
