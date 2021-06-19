import datetime
print(datetime.datetime.now().hour)

"""
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging
from telegram.ext import Updater
updater = Updater(
    token='1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM', use_context=True)
dispatcher = updater.dispatcher
# logging.basicConfig(
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def hello(update, context):
    context.bot.send_message(
        chat_id=889863862, text="I'm a bot, please talk to me! {}".format(update.effective_chat.id))


start_handler = CommandHandler('send', hello)
dispatcher.add_handler(start_handler)
updater.start_polling()
"""
