with open('pb.txt' , 'rt') as data:    

    for line in data.readlines():
         work_data = line    

    menu_continue = 1
    end = 1
    add =''    
    while menu_continue != 0:
       
        choise = input(' 1 - просмотр записей\n 2 - добавление записи\n 3 - поиск\n 4 - выход    \n')
       
        if choise == "1": #просмотр
            temp = work_data.split(';')
            for i in range (len(temp)):
                print(temp[i])
                
        
        if choise == "2":#добавление 
            add = ""           
            add += input("Введите имя: ").capitalize()
            add+=" "
            add += input("Введите фамилию: ").capitalize()
            add+=" "
            add += input("Введите номер телефона: ").lower()
            add+=" "
            add += input("Введите описание к записи: ").lower()
            add+=";"
            end = 1
       
            while end != 0:            
                add_confirm = input(f'{add}\nЗапись корректна ? ( да / нет ): ').lower()
           
                if add_confirm == "да":
                    work_data += add
                    end = 0

                elif add_confirm == "нет": 
                    choice1 = 2
                    end = 0            
                
                else: print("Введите 'да' или 'нет'")    
        
        # if choise1 == "3":#удаление
        
        
        if choise == "3":#поиск
            find_result = ''
            find = input('Введите искомое значение: ')
            base = []
            deep_base = []
            find_result = []
            base = work_data.split(';')   
            
            for i in range (len(base)):
                print(f'i{i} = {base[i]}')                
                deep_base = base[i].split(' ')

                for j in range (len(deep_base)):
                    
                    print(f'deepbase[{j}] = {deep_base[j]}')
                    if deep_base[j] == find:
                        find_result.append(base[i])
                        
            print(f'\nИскомая запись\n')
            for i in range(len(find_result)):
                print(find_result[i])
            print()
       
        if choise == "4":#выход
            with open('pb.txt' , 'w') as data:
                data.writelines(work_data)
                break
                




