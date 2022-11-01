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

    bot.send_message(message.chat.id, f'Привет, красотка! Добро пожаловать в наш салон красоты "Lavanda"💜', reply_markup=markup)
                                       
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
            bot.send_message(message.chat.id, text="Хочешь записаться?😍", reply_markup=markup)

        elif message.text == 'Услуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Прайс лист")

            btn3 = types.KeyboardButton("Хочу записаться!")
            markup.add(btn1, btn3)
            bot.send_message(message.chat.id, text="В нашем салоне красоты, ты можешь сделать:\
                                                        🌸Окрашивание волос\
                                                        🌸Красивую стрижку или укладку\
                                                        🌸Маникюр, педикюр", reply_markup=markup)
        elif message.text == 'Записаться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn4 = types.KeyboardButton("Стрижка, укладка")
            btn5 = types.KeyboardButton("Окрашивание")
            btn6 = types.KeyboardButton("Маникюр, педикюр")
            markup.add(btn4, btn5, btn6)
            bot.send_message(message.chat.id, 'Какую услугу хочешь получить?',reply_markup=markup )

        elif message.text == "Хочу записаться!":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id,"Супер! Оставь, пожалуйста, свой номер телефона и имя, чтобы мастер связался с тобой и договорился об удобном времени⏰", reply_markup = markup)
            bot.send_message(message.chat.id,"Если не хочешь ждать звонка, нажми на кнопку, чтобы позвонить нам.", reply_markup = markup)
            bot.send_message(message.chat.id, "С нетерпением ждем тебя в нашем салоне красоты, дорогая!🥰", reply_markup = markup)
            bot.send_message(message.chat.id,  "+996507240507", reply_markup=markup)

        elif message.text == "Еще подумаю":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn7 = types.KeyboardButton("Позвать специалиста")
            markup.add(btn7)
            bot.send_message(message.chat.id,"Хорошо, дорогая!🥰Если будут вопросы, обязательно задавай-специалист подключится к диалогу и поможет тебе.",reply_markup = markup)
            bot.send_message(message.chat.id,"Ждем тебя в нашем салоне красоты!",reply_markup = markup)

        elif message.text == "Стрижка, укладка":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id,"Супер! Оставь, пожалуйста, свой номер телефона и имя, чтобы мастер связался с тобой и Договорился об удобном времени⏰", reply_markup = markup)
            bot.send_message(message.chat.id,"Если не хочешь ждать звонка, нажми на кнопку, чтобы позвонить нам.", reply_markup = markup)
            bot.send_message(message.chat.id, "С нетерпением ждем тебя в нашем салоне красоты, дорогая!🥰", reply_markup = markup)
            bot.send_message(message.chat.id,  "+996507240507", reply_markup=markup)

        elif message.text == "Окрашивание":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id,"Супер! Оставь, пожалуйста, свой номер телефона и имя, чтобы мастер связался с тобой и Договорился об удобном времени⏰", reply_markup = markup)
            bot.send_message(message.chat.id,"Если не хочешь ждать звонка, нажми на кнопку, чтобы позвонить нам.", reply_markup = markup)
            bot.send_message(message.chat.id, "С нетерпением ждем тебя в нашем салоне красоты, дорогая!🥰", reply_markup = markup)
            bot.send_message(message.chat.id,  "+996507240507", reply_markup=markup)

        elif message.text == "Маникюр, педикюр":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id,"Супер! Оставь, пожалуйста, свой номер телефона и имя, чтобы мастер связался с тобой и Договорился об удобном времени⏰", reply_markup = markup)
            bot.send_message(message.chat.id,"Если не хочешь ждать звонка, нажми на кнопку, чтобы позвонить нам.", reply_markup = markup)
            bot.send_message(message.chat.id, "С нетерпением ждем тебя в нашем салоне красоты, дорогая!🥰", reply_markup = markup)
            bot.send_message(message.chat.id,  "+996507240507", reply_markup=markup)




bot.polling(none_stop=True)








