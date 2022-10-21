with open('pb.txt' , 'rt') as data: # автоматически закрывает файл
    
# data.readlines()
    for line in data.readlines():
         work_data = line
    # print(work_data.split())

    menu_continue = 1
    end = 1
    add =''
    spisok = []
    while menu_continue != 0:
       
        choise1 = input(' 1 - просмотр записей\n 2 - добавление записи\n 3 - удаление записи  \n 4 - поиск\n 5 - выход    \n')
       
        if choise1 == "1":
            temp = work_data.split(';')
            for i in range (len(temp)):
                print(temp[i])
                
        
        if choise1 == "2":  
            add = ""           
            add += input("Введите имя: ")
            add+=" "
            add += input("Введите фамилию: ")
            add+=" "
            add += input("Введите номер телефона: ")
            add+=" "
            add += input("Введите описание к записи: ")
            add+=" "
            end = 1
       
            while end != 0:            
                add_confirm = input(f'{add}\nЗапись корректна ? ( да / нет ): ')
           
                if add_confirm == "да":
                    work_data += ""
                    work_data += add
                    end = 0

                elif add_confirm == "нет": 
                    choice1 = 2
                    end = 0            
                
                else: print("Введите 'да' или 'нет'")    
        
        # if choise1 == "3":#удаление
        if choise1 == "4":#поиск
            find = work_data.split(';')
            base = []
            for i in range (len(find)):
                base[i] = find[i]
                print(find[i])

        if choise1 == "5":#выход
            with open('pb.txt' , 'w') as data:
                data.writelines(work_data)
                break
                




