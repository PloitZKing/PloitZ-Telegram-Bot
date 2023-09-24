from flask import Flask, request
import telebot
import os

# Initialize Flask app
app = Flask(__name__)

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
API_TOKEN = os.environ['TOKEN']

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Define a route for handling incoming updates from Telegram
@app.route('/telegram_webhook', methods=['POST'])
def telegram_webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return "ok", 200

# Define a command handler
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Howdy, how are you doing? I'm your assistant from PloitZ. To get started type /help"
    )

# Define a command handler for /socials
@bot.message_handler(commands=['socials', 'social'])
def socials(message):
    bot.reply_to(
        message,
        "Instagram - https://instagram.com/unofficialdxnny \n GitHub - https://github.com/unofficialdxnny"
    )

# Define a command handler for /snapify
@bot.message_handler(commands=['snapify'])
def snapify(message):
    bot.reply_to(
        message,
        "Snapify Help : Usage and Installation\nTutorial: https://www.youtube.com/watch?v=hDoJOp8Ysec1x\n\nDownload: https://github.com/unofficialdxnny/SnapRevive"
    )

# Define a command handler for /help
@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = "Here are the available commands:\n"
    help_text += "/start or /hello - Start a conversation\n"
    help_text += "/help - Display this help message\n"
    help_text += "/socials - Get link to social media\n"
    help_text += "/snapify - Get help with snapify"
    bot.reply_to(message, help_text)

# Define a message handler for new chat members
@bot.message_handler(func=lambda message: message.new_chat_members)
def welcome_new_members(message):
    for new_member in message.new_chat_members:
        bot.send_message(
            message.chat.id,
            f"Welcome, {new_member.first_name}! Thanks for joining the chat."
        )

# Define a message handler for members leaving the chat
@bot.message_handler(func=lambda message: message.left_chat_member)
def leave_chat_member(message):
    bot.send_message(
        message.chat.id,
        f"{message.left_chat_member.first_name} has left the chat."
    )

# Define a command handler for /online
@bot.message_handler(commands=['online'])
def check_online(message):
    bot.send_message(message.chat.id, "I'm online and ready to assist you!")

# Start the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
