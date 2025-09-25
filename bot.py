from flask import Flask, request
import telebot
import os

API_TOKEN = '7646070663:AAFv2Av2GxygxjVnhE3b5pay6MjkT3bjp4I'
WEBHOOK_URL = 'https://telegram-d6fu.onrender.com>/bot'  # Render app URL'inle değiştir
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Basit örnek komut
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Quantum Network Bot is online! ⚡")

# Webhook endpoint
@app.route('/bot', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    # Webhook ayarla
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
