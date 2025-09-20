from flask import Flask, send_file
import telebot

API_TOKEN = "7646070663:AAFv2Av2GxygxjVnhE3b5pay6MjkT3bjp4I"
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Web sayfasını sun
@app.route("/")
def index():
    return send_file("index.html")  # HTML ayrı dosya olmalı

# Bot polling'i ayrı threadte çalıştırabiliriz
import threading
def start_bot():
    bot.infinity_polling()

threading.Thread(target=start_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
