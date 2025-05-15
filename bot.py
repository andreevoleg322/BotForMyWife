from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
from messages import RandomMessages, NoticeMessages
import time

# Токен вашего бота (замените на свой)
TOKEN = "7461717869:AAG_Z6t397efULdJh8Z4AUxgm1DUyX94CpU"
# ID чата с женой (можно узнать через @userinfobot)
CHAT_ID = 471783827

# Инициализация бота
bot = Bot(token=TOKEN)
msg_generator = RandomMessages()
notice = NoticeMessages()
updater = Updater(token=TOKEN, use_context=True)

def start(update, context):
    update.message.reply_text(
        "Привет, любимая!\n"
        "Я буду присылать тебе приятные сообщения и напоминания.\n"
    )

updater.dispatcher.add_handler(CommandHandler("start", start))
# Функции для отправки сообщения
def send_morning_message():
    message = msg_generator.get_random_morning_message()
    bot.send_message(chat_id=CHAT_ID, text=message)

def send_compliment_message():
    message = msg_generator.get_random_compliment_message()
    bot.send_message(chat_id=CHAT_ID, text=message)

def send_notice_message_water():
    message = notice.get_notice_drink_water()
    bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Отправлено: {message}")

def send_notice_message_workout():
    message = notice.get_notice_workout()
    bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Отправлено: {message}")

def send_notice_message_close_inst():
    message = notice.get_notice_close_insta()
    bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Отправлено: {message}")

scheduler = BackgroundScheduler()

scheduler.add_job(send_morning_message, 'cron', hour=8, minute=30)
scheduler.add_job(send_compliment_message(), 'cron', hour=12, minute=00)
scheduler.add_job(send_compliment_message(), 'cron', hour=15, minute=00)
scheduler.add_job(send_compliment_message(), 'cron', hour=18, minute=00)
scheduler.add_job(send_notice_message_workout(), 'cron', hour=13, minute=45)
scheduler.add_job(send_notice_message_workout(), 'cron', hour=14, minute=45)
scheduler.add_job(send_notice_message_workout(), 'cron', hour=15, minute=45)
scheduler.add_job(send_notice_message_workout(), 'cron', hour=16, minute=45)
scheduler.add_job(send_notice_message_workout(), 'cron', hour=17, minute=45)
#scheduler.add_job(send_notice_message_water(), 'interval', hours=2)
scheduler.add_job(send_notice_message_water(), 'cron', hour=11, minute=30)
scheduler.add_job(send_notice_message_water(), 'cron', hour=13, minute=30)
scheduler.add_job(send_notice_message_water(), 'cron', hour=15, minute=30)
scheduler.add_job(send_notice_message_water(), 'cron', hour=17, minute=30)
scheduler.add_job(send_notice_message_water(), 'cron', hour=19, minute=30)
scheduler.add_job(send_notice_message_close_inst(), 'cron', hour=14, minute=00)
scheduler.add_job(send_notice_message_close_inst(), 'cron', hour=17, minute=00)

scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()
    updater.stop()