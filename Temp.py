def add_users_admin():
    while True:
        work_data = ie.read_file("users.txt")    
        view.view_base("users.txt")
        result = str("")
        first_name = input('Введите имя: ')
        result += first_name.capitalize()
        last_name = input('Введите фамилию: ')
        result += "," + last_name.capitalize()
        print('Задайте роль : ')
       
        role = menu.role_menu()      
        if role == "1": role = "admin"
        if role == "2": role = "teacher"
        if role == "3": role = "student"        
        result += "," + role
        if result in work_data: 
            print('Такой пользователь есть в базе')
            return()
        else:
            work_data.append(result)
            print(result)
            choise = input('Сохранить пользователя? Да  / Нет\n')
            if choise.lower() == "да":             
                temp=""
                for item in work_data:
                    temp = temp + (f'{item}\n')            
                ie.write_file("users.txt", temp)
                return()
            elif choise.lower() == "нет":
                return()