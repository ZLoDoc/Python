import telebot.types
import random
from telebot import TeleBot
 
 
bot = TeleBot('5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg')


def name_choice_step():
   
    con = dict()
    first = int(random.randrange(0,2))
    con["first"] = first
    candy = int(input('Сколько конфет на кону? : '))
    con['candy'] = candy
    chose = 1
    while chose > 0: 
        choice = int(input('\n\n\n\n\nвыбири вариант игры: 1 - с человеком, 2 - с компом, 3 - c непобедимым: '))
        con['choice'] = choice
        if 0 >= choice or choice > 3: 
            continue
        else: chose = chose-1
      
        player_1name = input('Имя первого игрока ?: ')
        # player_1name ='Вася'
                
        if choice == 1:    
            player_2name = input('Имя второго игрока ?: ')
            # player_2name = 'Катя'        
        if choice == 2:    
            player_2name = 'Comp'
        if choice == 3:    
            player_2name = 'Bot'
                    
        print(f'\nПриветствую вас {player_1name} и {player_2name} !!!!')
        if first == 1:
            print(f'\nПервым ходит {player_1name}')
        if first == 0: 
            temp = player_1name
            player_1name = player_2name
            player_2name = temp
            print(f'\nПервым ходит {player_1name}')
        con['player_1name'] = player_1name
        con['player_2name'] = player_2name     
    return (con)

def players_algorithm(con):
    flag = 1
    candy = con["candy"]
    while candy >= 0:
        print(f'на столе {candy} конфет')
        if flag == 1:
                player = con["player_1name"]
        if flag == 0:
                player = con["player_2name"]
        step = int(input(f'\t {player} возьми не больше 28 конфет :'))
        if 0 < step <= 28 : 
            candy = candy - step
            if candy <=0:
                return player
            if flag == 1 : flag = 0
            else: flag = 1
    
        else: 
            continue
# ____________________________________________________________________________,

def comp_algorithm(con):
    flag = 1
    candy = con["candy"]
    while candy >= 0:
        print(f'на столе {candy} конфет')
        if flag == 1:
                player = con["player_1name"]
        if flag == 0:
                player = con["player_2name"]
        if player == 'Comp':
            step = int(random.randrange(1,29))
            print (f'\t{player} взял {step} конфет')
        if player != 'Comp':            
            step = int(input(f'\n\t {player} возьми не больше 28 конфет :'))
        if 0 < step <= 28 : 
            candy = candy - step
            if candy <= 0:
                return player
            if flag == 1 : flag = 0
            else: flag = 1
        
        else: 
            continue
# ____________________________________________________________________________,
def bot_algorithm(con):
    flag = 1
    candy = con["candy"]
    first_step = 0
    while candy >= 0:
        print(f'на столе {candy} конфет')
        
        if flag == 1:
            player = con["player_1name"]
        if flag == 0:
            player = con["player_2name"]
        
        if player == 'Bot':
            if first_step == 0:
                step = (candy - (int(candy / 29) * 29))-1                
                first_step = 1
            elif first_step != 0:
                step = 29 - player_step
            print (f'\t{player} взял {step} конфет')
        
        if player != 'Bot':            
            step = int(input(f'\n\t {player} возьми не больше 28 конфет :'))
            player_step = step 

        if 0 < step <= 28 : 
            candy = candy - step
            if candy <=0:
                return player
            if flag == 1 : flag = 0
            else: flag = 1
        
        else: 
            continue
        # ____________________________________________________________________________,
def choice(choise):
    a = (name_choice_step())
    if a["choice"] == 1: print(f'Игрок {players_algorithm(a)} проиграл !')
    if a["choice"] == 2: print(f'Игрок {comp_algorithm(a)} проиграл !')
    if a["choice"] == 3: print(f'Игрок {bot_algorithm(a)} проиграл !')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#  bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#  bot.reply_to(message, message.text)

def summator(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'Это некорректный запрос'

@bot.message_handler(commands=['candle'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="1 - Игра с человеком\n2 - Игра с компом\n2 - Игра с Вot-ом")
    bot.register_next_step_handler(callback=choice, choice=msg)
 
 


bot.polling()