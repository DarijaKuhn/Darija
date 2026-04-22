import telebot

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def main_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = telebot.types.KeyboardButton("Помощь 🆘")
    btn2 = telebot.types.KeyboardButton("О проекте ℹ️")

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}! Выбери действие:", reply_markup=markup)

bot.polling(none_stop=True)
