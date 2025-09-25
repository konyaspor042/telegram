import telebot
from flask import Flask, request
import os
import requests

API_TOKEN = "7646070663:AAFv2Av2GxygxjVnhE3b5pay6MjkT3bjp4I"
WEBHOOK_URL = "https://telegram-4-2vb8.onrender.com/bot"  # Render URL'in /bot ile

bot = telebot.TeleBot(API_TOKEN, threaded=False)
app = Flask(__name__)

# === BOT KOMUTLARI ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Bot aktif! Webhook üzerinden çalışıyor.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Mesajını aldım: {message.text}")

# === FLASK ROUTES ===
@app.route("/bot", methods=['POST'])
def getMessage():
    json_str = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/", methods=['GET'])
def index():
    return "Quantum Bot Çalışıyor ✅", 200

# === Webhook ayarlama ve Flask başlatma ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    
    # Önce eski webhook'u kaldır, sonra yeni webhook'u set et
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    print(f"Webhook ayarlandı: {WEBHOOK_URL}")
    app.run(host="0.0.0.0", port=port)
