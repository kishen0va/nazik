# import telebot
# from telebot import types
# from config import TOKEN

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Прайс лист")
#     btn2 = types.KeyboardButton("Услуги")
#     btn3 = types.KeyboardButton("Хочу записаться!")
#     markup.add(btn1, btn2)

#     bot.send_message(message.chat.id, f'Привет, красотка! Добро пожаловать в наш салон красоты "Lavanda"')
                                       
#     bot.send_message(message.chat.id, f' Для новых клиентов у нас действует скидка 10% обязательно ею воспользуйся!')
                                       
#     bot.send_message(message.chat.id, f' Какую информацию прислать?')

# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "Прайс лист"):
#         bot.send_message(message.chat.id, text="А вот и цены за наши услуги. Если ты у нас первый раз, то сделаем еще скидку 10%")
#         bot.send_message(message.chat.id, text="Хочешь записаться?")
    # elif(message.text == "❓ Задать вопрос"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton("Как меня зовут?")
    #     btn2 = types.KeyboardButton("Что я могу?")
    #     back = types.KeyboardButton("Вернуться в главное меню")
    #     markup.add(btn1, btn2, back)
    #     bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Прайс лист")
    btn2 = types.KeyboardButton("Услуги")
    btn3 = types.KeyboardButton("Хочу записаться!")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, f'Привет, красотка! Добро пожаловать в наш салон красоты "Lavanda"', reply_markup=markup)
                                       
    bot.send_message(message.chat.id, f' Для новых клиентов у нас действует скидка 10% обязательно ею воспользуйся!', reply_markup=markup)
                                       
    bot.send_message(message.chat.id, f' Какую информацию прислать?', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Прайс лист':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            n1 = types.KeyboardButton('Записаться')
            n2 = types.KeyboardButton('Еще подумаю')
            markup.add(n1,n2)
            bot.send_message(message.chat.id, text="А вот и цены за наши услуги. Если ты у нас первый раз, то сделаем еще скидку 10%",reply_markup=markup)
            bot.send_message(message.chat.id, text="Хочешь записаться?", reply_markup=markup)

        elif message.text == 'Услуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Прайс лист")
            btn3 = types.KeyboardButton("Хочу записаться!")
            markup.add(btn1, btn3)
            
            
#         elif message.text == 'Audi Q7':
#             bot.send_message(message.chat.id, 'Новый Audi Q7 2020 года создан разрушать \
#                 границы путешествий, дарить полную свободу комфорта. Автомобиль каждой деталью излучает\
#                 мощь и динамику, при этом поражает изысканной элегантностью. Он прекрасен не только снаружи, \
#                 но и внутри, обеспечивая максимум условий для наслаждения любым мгновением поездки.\
#                 1 Бездорожье является его стихией, о чем свидетельствует большой дорожный просвет в сочетании с полным приводом.\
#                 В то же время, благодаря расширенному набору опциональных настроек, внедорожник отлично приспособлен к городским условиям.\
#                 Узнайте больше о возможностях и новых технологиях.')
#             photo = open('', 'rb')
#             photo2 = open('', 'rb')
#             photo3 = open('', 'rb')
#             bot.send_photo(message.chat.id, photo)
#             bot.send_photo(message.chat.id, photo2)
#             bot.send_photo(message.chat.id, photo3)
bot.polling(none_stop=True)








