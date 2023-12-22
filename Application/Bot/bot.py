# from typing import Union
#
# from telegram import Bot
# from telegram.ext import Updater, MessageHandler, filters
#
#
# # Replace 'YOUR_BOT_TOKEN' with the actual API token provided by BotFather
# UPDATER = None
#
#
# def start(update, context):
#     update.message.reply_text('Hello! I am your Telegram bot.')
#
#
# def echo(update, context):
#     # Echo the user's message back to the group
#     update.message.reply_text(update.message.text)
#
# def main():
#     # Create an Updater instance with your bot's token
#     updater = Updater(Bot(token=), )
#
#     # Get the dispatcher to register handlers
#     dp = updater.dispatcher
#
#     # Register a command handler for the /start command
#     dp.add_handler(MessageHandler(filters.command("/start"), start))
#
#     # Register an echo handler to respond to text messages
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#
#     # Start the bot
#     updater.start_polling()
#
#     # Run the bot until you send a signal (e.g., Ctrl+C)
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
