import emoji

def emoji_change(string):
    if string == "X":
        string = emoji.emojize(":cross_mark:")
    elif string == "O":
        string = emoji.emojize(":hollow_red_circle:")
    return string



tic = [[1,2,3],
       [4,5,6],
       [7,8,9]]
game = 1
flag = 1
result = []
for i in range(len(tic)):         
    print(['{:^3}'.format(i) for i in tic[i][:]])
while game > 0:

    if flag == 1: a = int(input('Поставте Х :'))
    if flag == 0: a = int(input('Поставте O :'))

    

    for k in range(len(tic)):
        for n in range(len(tic)):                
            if tic[k][n]  == a :
                if flag == 1:
                    tic[k][n] = emoji.emojize(":cross_mark:")
                    flag = 0
                    continue
                if flag == 0:
                    tic[k][n] = emoji.emojize(":hollow_red_circle:")
                    flag = 1
                    continue
    for i in range(len(tic)): 
        print(['{:^3}'.format(i) for i in tic[i][:]])
    print()
    
# проверка победы
    if  (tic[0][0]) == (tic[0][1]) == (tic[0][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    if  (tic[1][0]) == (tic[1][1]) == (tic[1][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    if  (tic[2][0]) == (tic[2][1]) == (tic[2][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    # горизонтали


    if  (tic[0][0]) == (tic[1][0]) == (tic[2][0]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    if  (tic[0][1]) == (tic[1][1]) == (tic[2][1]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    if  (tic[0][2]) == (tic[1][2]) == (tic[2][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    # вертикали
    
    
    
    if  (tic[0][0]) == (tic[1][1]) == (tic[2][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    if  (tic[2][0]) == (tic[1][1]) == (tic[0][2]) == emoji.emojize(":cross_mark:"):
        print(f' {emoji.emojize(":cross_mark:")} - победил')
        break
    # диагонали
    
      
    if  (tic[0][0]) == (tic[0][1]) == (tic[0][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    if  (tic[1][0]) == (tic[1][1]) == (tic[1][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    if  (tic[2][0]) == (tic[2][1]) == (tic[2][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    # горизонтали

    if  (tic[0][0]) == (tic[1][0]) == (tic[2][0]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    if  (tic[0][1]) == (tic[1][1]) == (tic[2][1]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    if  (tic[0][2]) == (tic[1][2]) == (tic[2][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    # вертикали

    if  (tic[0][0]) == (tic[1][1]) == (tic[2][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break
    if  (tic[2][0]) == (tic[1][1]) == (tic[0][2]) == emoji.emojize(":hollow_red_circle:"):
        print(f' {emoji.emojize(":hollow_red_circle:")} - победил')
        break            