import telebot
import password
from telebot import types

token1 = password.token
bot = telebot.TeleBot(token1)

class First_buttons:
   @bot.message_handler(commands=['start'])
   def f_buttons(command):
      keyboard = telebot.types.InlineKeyboardMarkup()
      keyboard.add(telebot.types.InlineKeyboardButton(text = 'USD', callback_data = 'USD'))
      keyboard.add(telebot.types.InlineKeyboardButton(text = 'RUR', callback_data = 'RUR'), telebot.types.InlineKeyboardButton(text = 'EUR', callback_data = 'EUR'))
      bot.send_message(command.chat.id, 'Выберите валюту для обмена', reply_markup=keyboard)
      
   @bot.callback_query_handler(func=lambda call: True)
   def f_back_data(call):
      bot.send_message(call.message.chat.id, f"Вы выбрали {call.data} для обмена \n\n Для выбора валюты на которую вы хотите обмнять нажмите: /exchange\n")
      
class Second_buttons:
   @bot.message_handler(commands=['exchange'])
   def s_buttons(command):
      keyboard = telebot.types.InlineKeyboardMarkup()
      keyboard.add(telebot.types.InlineKeyboardButton(text = 'USD', callback_data = 'USD'))
      keyboard.add(telebot.types.InlineKeyboardButton(text = 'RUR', callback_data = 'RUR'), telebot.types.InlineKeyboardButton(text = 'EUR', callback_data = 'EUR'))
      bot.send_message(command.chat.id, 'Выберите валюту на которую хотите провести обмен', reply_markup=keyboard)
   
   @bot.callback_query_handler(func=lambda call: True)
   def s_back_data(call):
      bot.send_message(call.message.chat.id, f"Ваша валюта будет обменена на {call.data}\n\n Сообщите сколько вы хотите обменять, введите: /money")

   @bot.message_handler(commands=['money'])
   def write_quantity(command):
      bot.send_message(command.message.chat.id, "Введите количество для обмена:")
      
class Hello:
   @bot.message_handler(content_types=['text'])
   def hello_word(message):
      if message.text == "1": #число
         bot.send_message(message.chat.id, "Я не понимаю чисел, введи текст!")
      elif message.text == "hey": #текст на английском
         bot.send_message(message.chat.id, "Я не понимаю английского языка, пиши по русски")
      elif message.text == "/":#символы
         bot.send_message(message.chat.id, "Что за каракули? Пиши тест")
      elif message.text == "ее":#текст на руссом
         bot.send_message(message.chat.id, "Обычно все люди начинают беседу с привета...")
      else:
         bot.send_message(message.chat.id, "Привет, я Валютный бот\nДля начала обмена нажмите: /start")

bot.polling(none_stop=True, interval=0)
