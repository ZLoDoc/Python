def add_data(work_data):#добавление 

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
    return work_data