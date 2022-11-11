import telebot
from telebot import TeleBot
import random


# токен
bot = TeleBot('5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg')

user_dict = {}


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.age = None
#         self.sex = None

candy=0
step=0

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, "Привет мы начинаем игру в конфетки.\n Нужно брать со стола конфеты,но не больше 28 штук за 1 ход. Кто возъмёт последнюю - тот проиграл= )\nНапиши сколько конфет лежит на столе?")    
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    
    global candy
    try:        
        candy = message.text
        msg = bot.reply_to(message, f'Ты положил на стол {message.text} конфет\n Сколько возьмешь ?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_age_step(message):
    global step
    print(f'step1 = {step}')
    try:
        
        step = message.text
        if not step.isdigit():
            msg = bot.reply_to(message, 'Введено не числовое значение. \nВведит правильно:')
            print(f'step2 = {step}')
            bot.register_next_step_handler(msg, process_age_step)
            return
        elif step < 0 or step > 28:
            msg = bot.reply_to(message, f'{message.text} - Ты взял не правильное количество конфет. Возьми не меньше 0 и не больше 28 :')
            print(f'step3 = {step}')
            bot.register_next_step_handler(msg, process_age_step)            
            return
        print(f'step4 = {step}')
    except Exception as e:
        bot.reply_to(message, 'oooops')


# def process_age_step(message):
#     global step
#     global candy 
#     print (f'step1 = {step}')
#     try:
#         if step>=0 or step <=28 or candy - step > 0:
#             step = message.text
#             print (f'step2 = {step}')
#             msg = bot.reply_to(message, f'Ты взял {message.text} конфет')
#         elif step < 0 or step > 28:
#             msg = bot.reply_to(message, f'{message.text} - Ты взял не правильное количество конфет. Возьми не меньше 0 и не больше 28 :')
#             bot.register_next_step_handler(msg, process_age_step)    
#             return
#         elif not step.isdigit():
#             msg = bot.reply_to(message, f'{message.text} - не число. Напиши сколько конфет возьмешь:')
#             bot.register_next_step_handler(msg, process_age_step)
#             return
#     except Exception as e:
#         bot.reply_to(message, 'oooops')

# def process_sex_step(message):
#     try:
#         chat_id = message.chat.id
#         sex = message.text
#         user = user_dict[chat_id]
#         if (sex == u'Male') or (sex == u'Female'):
#             user.sex = sex
#         else:
#             raise Exception("Unknown sex")
#         bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.infinity_polling()    