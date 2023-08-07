from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define your Telegram bot token here
TOKEN = '6478802023:AAHznSCD1JbwhnQbrA2yJ8qGUTIZZQLkmJ8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Feedback Bot! Please provide your feedback.")

def collect_feedback(update: Update, context: CallbackContext) -> None:
    user_feedback = update.message.text
    user_id = update.message.from_user.id
    
    # You can save the feedback to a database or file here
    with open('feedback.txt', 'a') as feedback_file:
        feedback_file.write(f"User ID: {user_id}\nFeedback: {user_feedback}\n\n")
    
    update.message.reply_text("Thank you for your feedback!")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command to start the bot
    dispatcher.add_handler(CommandHandler("start", start))

    # Collect feedback from user messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, collect_feedback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
