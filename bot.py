import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur WinAlert Bot !")

if __name__ == "__main__":
    print("Le bot est en ligne...")
    bot.infinity_polling()
