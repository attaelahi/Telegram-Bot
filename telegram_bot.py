from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# Define the start command handler
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram Bot.")

# Define the help command handler
def help(update: Update, context: CallbackContext):
    help_text = "Here are the available commands:\n/start - Start the bot\n/help - Show this help message"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater('7131264114:AAHuUlHbHRnzRbsNprSM6y6GHDsw-e3oHe8', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)

    # Register command handlers with the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
