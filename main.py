# t.me/lab7_fir_bot
import psycopg2
import telebot
from telebot import types

token = "5809232144:AAEwlBXXWZo-pzj-FsQJBWgKTFILvu8cgTA"
bot = telebot.TeleBot(token)

# Подключаемся к базе данных с расписанием
conn = psycopg2.connect(database="schedule_db",
                        user="lab7",
                        password="lab7",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

# Начало работы
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею выдавать расписание - как на конкретный день, так и на всю неделю :3')

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Oфициальный сайт МТУСИ: https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def start_message(message):
    bot.send_message(message.chat.id, 'Сейчас чётная неделя')

# Обращение к БД и получение расписания для конкретного дня недели
def get_schedule_for_day(day):
    cursor.execute(f"SELECT * FROM timetable JOIN subject on timetable.sub_id = subject.sub_id JOIN teacher on "
                   f"teacher.sub_id = subject.sub_id WHERE day = '{day}'")
    res = list(cursor.fetchall())
    if len(res) == 0:
        return "Кажется, в этот день нет пар."
    else:
        items = []
        for res_item in res:
            items.append(
                f"Предмет: {res_item[6]}\nНачало: {res_item[4]}\nАудитория: {res_item[3]}\nПреподаватель: {res_item[8]}\n"
            )
        return "\n".join(items)
def get_schedule_for_days(days):
    days_items = []
    for day in days:
        days_items.append(f"{day}\n{get_schedule_for_day(day)}")
    return "\n-----------------\n".join(days_items)

@bot.message_handler(content_types=['text'])
def answer(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Вся неделя")

    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Ты можешь выбрать как конкретный день, так и всю неделю', reply_markup=keyboard)

    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    if message.text in days:
        res = get_schedule_for_day(message.text)
        bot.send_message(message.chat.id, res, reply_markup=keyboard)

    if message.text == "Вся неделя":
        res = get_schedule_for_days(days)
        bot.send_message(message.chat.id, res, reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, "Я не понимаю(")


print("bot started :3")
bot.polling(none_stop=True, interval=0)
