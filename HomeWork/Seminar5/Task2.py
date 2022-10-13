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
# player_1name = input('Имя первого игрока ?')
player_1name ='Вася'
print(f'\nЗдравствуй {player_1name}')
# player_2name = input('Имя второго игрока ?')
player_2name = 'Катя'
print(f'\nЗдравствуй {player_2name}')
саndy = 30
print(f'\nна столе {саndy} конфет')

while саndy >= 0:
    player_1 = int(input(f'\n\t {player_1name} возьми не больше 28 конфет :'))
    if 0 < player_1 <= 28 : 
        саndy = саndy - player_1
        if саndy <=0:
            print(f'{player_1name} проиграл')
            break

        print(f'\nна столе {саndy} конфет')
    else:
        continue
    player_2 = int(input(f'\n\t {player_2name} возьми не больше 28 конфет :'))
    if 0 < player_2 <= 28 : 
        саndy = саndy - player_2
        if саndy <=0:
            print(f'{player_2name} проиграл')
            break
        print(f'\nна столе {саndy} конфет')
    else:
        continue
    
        # else:
        #     print(f'\nна столе {саndy} конфета')
        #     comp = int(random.randrange(0,5))
        #     print(f'\n\tя взял {comp} конфет')
        #     саndy = саndy - comp