import threading
from flask import Flask, send_file
import telebot
import time

API_TOKEN = '7646070663:AAFv2Av2GxygxjVnhE3b5pay6MjkT3bjp4I'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Quantum Network Bot is online! ⚡")

def start_bot():
    bot.infinity_polling()

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

def start_flask():
    app.run(host='0.0.0.0', port=3000)

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    threading.Thread(target=start_flask).start()
    while True:
        time.sleep(10)
