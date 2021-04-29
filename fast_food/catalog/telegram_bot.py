import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


def hello(update, context):
    print(update.message.user)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main():
    updater = Updater("1769249243:AAHDyKX-QmuITwSxKqtbqpNtB0sVSu_dzaY")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', hello))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# updater = Updater('YOUR TOKEN HERE')
#
# updater.dispatcher.add_handler(CommandHandler('hello', hello))
#
# updater.start_polling()
# updater.idle()
