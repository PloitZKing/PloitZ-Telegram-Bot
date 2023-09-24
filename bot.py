import telebot
import os
import keep_alive

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
API_TOKEN = os.environ['TOKEN']

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)


# Define a command handler
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(
      message,
      "Howdy, how are you doing? Im your assistant from PloitZ. To get started type /help"
  )


@bot.message_handler(commands=['socials', 'social'])
def socials(message):
  bot.reply_to(
      message,
      "Instagram - https://instagram.com/unofficialdxnny \n GitHub - https://github.com/unofficialdxnny"
  )


@bot.message_handler(commands=['snapify'])
def snapify(message):
  bot.reply_to(
      message,
      "Snapify Help : Usage and Installation\nTutorial: https://www.youtube.com/watch?v=hDoJOp8Ysec1x\n\nDownload: https://github.com/unofficialdxnny/SnapRevive"
  )


@bot.message_handler(commands=['help'])
def show_help(message):
  help_text = "Here are the available commands:\n"
  help_text += "/start or /hello - Start a conversation\n"
  help_text += "/help - Display this help message\n"
  help_text += "/socials - Get link to social media\n"
  help_text += "/snapify - get help with snapify"
  help_text += "/mailspammer - get help with gmail spammer"
  bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: message.new_chat_members)
def welcome_new_members(message):
  for new_member in message.new_chat_members:
    bot.send_message(
        message.chat.id,
        f"Welcome, {new_member.first_name}! Thanks for joining the chat.")


# Handle members leaving the chat
@bot.message_handler(func=lambda message: message.left_chat_member)
def leave_chat_member(message):
  bot.send_message(
      message.chat.id,
      f"{message.left_chat_member.first_name} has left the chat.")


# Handle the /online command
@bot.message_handler(commands=['online'])
def check_online(message):
  bot.send_message(message.chat.id, "I'm online and ready to assist you!")

@bot.message_handler(commands=['gmail', 'spammer', 'mailspammer'])
def snapify(message):
  bot.reply_to(
      message,
      "gmail spammer Help : Usage and Installation\nTutorial: https://github.com/unofficialdxnny/gmail-spammer"
  )


# Start the bot
keep_alive.keep_alive()
bot.infinity_polling()
