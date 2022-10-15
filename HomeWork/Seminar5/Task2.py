# Создайте программу для игры с конфетами человек против человека.
#   Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""

import random
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
            if candy <=0:
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
a = (name_choice_step())
if a["choice"] == 1: print(f'Игрок {players_algorithm(a)} проиграл !')
if a["choice"] == 2: print(f'Игрок {comp_algorithm(a)} проиграл !')
if a["choice"] == 3: print(f'Игрок {bot_algorithm(a)} проиграл !')        