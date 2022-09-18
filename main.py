import telebot
import random
import time
#from datetime import datetime

time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute)

voprosi = []
pop = 3

with open('zadachi1.txt', encoding="UTF-8") as f:
    sob = f.readlines()
    for k in sob:
        k = k.split(')')
        k[0]+=')'
        voprosi+=[k]
#print(voprosi[0][0])
#print(voprosi[0][1])

random.shuffle(voprosi)
otv = voprosi[0][1]

#c = sqlite3.connect('zad.db', check_same_thread=False)
#cursor = c.cursor()

#def db_table_val(number: int, zad: text, otvet: int):
#  cursor.execute('INSERT INTO zad (number, zad, otvet) VALUES (?, ?, ?)', (number, zad, otvet))
#  conn.commit()

bot = telebot.TeleBot("")
BOT_URL = ''
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"""Привет, {message.from_user.first_name}
Сейчас я расскажу как тут все устроено, если ты в чат напишешь "Хочу решать физику", то бот отправит тебе одну задачу и проверит твой ответ
"""
    bot.send_message(message.chat.id, mess)

"""if time.hour == '20' and time.minute == '08':
    bot.send_message(message.chat.id, f'Время для задач по физике!')
else:
    bot.send_message(message.chat.id, time)"""


@bot.message_handler()
def get_user_text(message):
    if message.text == "Хочу решать физику":
        bot.send_message(message.chat.id, "Ты уверен, что тебе это надо?")
        bot.send_message(message.chat.id, voprosi[0][0])
        bot.register_next_step_handler(message, send_text)
    else:
        sti = open("srg.webp", "rb")
        bot.send_sticker(message.chat.id, sti)

#@bot.message_handler(content_types=['text'])

def send_text(message):
    x = str(message.text)
    print(x, type(x), voprosi[0][1], type(voprosi[0][1]))
    if x == voprosi[0][1]:
        bot.send_message(message.chat.id, 'Соточка по физике у тебя в кармане! Осталось еще немного поботать (целый год) и возможно порог перейдешь)')
        random.shuffle(voprosi)
    elif x != str(otv):
        bot.send_message(message.chat.id, 'Тебе не стоит сдавать физику...')
        bot.send_message(message.chat.id, 'Хочешь увидеть ответ?')
        bot.register_next_step_handler(message, vib)

def vib(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, otv)
        random.shuffle(voprosi)
    elif message.text == 'Нет':
        bot.register_next_step_handler(message, send_text)
    else:
        bot.send_message(message.chat.id, 'Напиши "Да" или "Нет" с большой буквы!')
        bot.register_next_step_handler(message, vib)

if __name__ == '__main__':
      bot.polling(none_stop=True)