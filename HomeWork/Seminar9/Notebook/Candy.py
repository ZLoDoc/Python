import telebot
from telebot import TeleBot
import random


# токен
bot = TeleBot('5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg')

candy_and_first_step = 0
step = 0
first = 2
comp = 0
player = 0
 

@bot.message_handler(commands=['start']) #начало игры запрос количества конфет
def start(message):
    global first
    global comp
    global player

    first = random.randrange(0,1)
    if first == 0:
        player = 1
    elif first == 1:
        comp = 1      
    
    if player == 1:
        bot.send_message(message.from_user.id, text='Ты ходишь первый')
        bot.send_message(message.from_user.id, text='Напиши сколько конфет лежит на столе ?')   
        print(message.text)
        print(first, comp, player) 
        bot.register_next_step_handler(message, candy_and_first_step)
    if comp == 1:
        bot.send_message(message.from_user.id, text='Comp ходит первый')
        bot.send_message(message.from_user.id, text='Напиши сколько конфет лежит на столе ?') 
        bot.register_next_step_handler(message,comp_algoritm)    


def candy_and_first_step(message):        
    global candy_and_first_step
    if message.text.isdigit():
        candy_and_first_step = int(message.text)
        print(f'candy_and_first_step1 = {candy_and_first_step}')
        bot.send_message(message.from_user.id, text=f'На столе лежит: {message.text} конфет')        
        bot.send_message(message.from_user.id, text='Возьми не больше 28 конфет')
        bot.register_next_step_handler(message, player_algorithm) 
    else:
        bot.send_message(message.from_user.id, text=f'Я не знаю цифер - {message.text}')
        bot.send_message(message.from_user.id, text='Введи количество конфет')       
        bot.register_next_step_handler(message, candy_and_first_step)        
        return


    
def player_algorithm(message):    
    global candy_and_first_step
    global step
    global comp
    global player
    if message.text.isdigit():
        step = int(message.text)
        print(f'step = {step}')       
        if step > 28:
            bot.send_message(chat_id=message.from_user.id, text='Нельзя брать больше 28 конфет')
            bot.send_message(message.from_user.id, text='Введи количество конфет')
            bot.register_next_step_handler(message, player_algorithm)
            return
        elif step  <= 0:
            bot.send_message(chat_id=message.from_user.id, text=f'Возьми хоть 1 конфету')
            bot.send_message(message.from_user.id, text='Введи количество конфет')
            bot.register_next_step_handler(message, player_algorithm)
            return
        elif  candy_and_first_step - step <= 0 :
            bot.send_message(chat_id=message.from_user.id, text=f'Тут всего лишь {candy_and_first_step} конфет')
            bot.send_message(message.from_user.id, text='Возьми не более {candy_and_first_step} конфет')
            bot.register_next_step_handler(message, player_algorithm)
            return
    else:
        bot.send_message(chat_id=message.from_user.id, text=f'Я не знаю цифер - {message.text}')
        bot.send_message(message.from_user.id, text='Введи количество конфет цифрами')
        bot.register_next_step_handler(message, player_algorithm)

    candy_and_first_step = candy_and_first_step - step
    print(f'candy_and_first_step_end_step_of_player = {candy_and_first_step}')
    if candy_and_first_step > 0 :
        player = 0
        comp = 1
    if candy_and_first_step <= 0:
        bot.register_next_step_handler(message, result_message)


def comp_algoritm(message):
    global candy_and_first_step
    global step
    global comp
    global player
    if candy_and_first_step - step <= 28:
        step = candy_and_first_step
    else:        
        step = random.randrage(1,29)
        bot.send_message(message.from_user.id, text='Комп взял {step} конфеток')
        candy_and_first_step = candy_and_first_step - step


    if candy_and_first_step > 0 :
        comp = 0
        player = 1
        
    if candy_and_first_step <= 0:
        bot.register_next_step_handler(message, result_message)



def result_message(message):
    global comp
    global player
    if player == 1:
        print(f'player_end{player}')
        bot.send_message(message.from_user.id, text='Ура ты выиграл')
    if comp == 1:
        print(f'comp_end{comp}')
        bot.send_message(message.from_user.id, text='Увы, но комп выиграл')

# def jopa(message):
#     global candy_and_first_step
#     global step
#     print(f'msg in jopa = {message.text}')
#     print(f'candy_and_first_step = {candy_and_first_step}')
#     print(f'step = {step}')
#     bot.send_message(chat_id=message.from_user.id, text=f'Здесь нет - {message.text} конфет')

bot.polling(none_stop=True)     