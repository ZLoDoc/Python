def bot_algorithm():
    flag = 1
    candy = 100
    first_step = 0
    while candy >= 0:
        print(f'на столе {candy} конфет')
        
        if flag == 1:
            player = 'aaaaaaa'
        if flag == 0:
            player = 'Bot'
        
        if player == 'Bot':
            if first_step == 0:
                step = (candy - (int(candy / 29) * 29))-1
                print(f'первый ход{step}')
                first_step = 1
            elif first_step != 0:
                step = 29 - player_step
            print (f'{player} взял {step} конфет')
        
        if player != 'Bot':            
            step = int(input(f'\n\t {player} возьми не больше 28 конфет :'))
            player_step = step 

        if 0 < step <= 28 : 
            candy = candy - step
            if candy <=0:
                # print(f'{player} проиграл')
                return player                

            # print(f'\nна столе {candy} конфет')
            if flag == 1 : flag = 0
            else: flag = 1
        
        else: 
            continue
print(f'Игрок {bot_algorithm()} проиграл !')