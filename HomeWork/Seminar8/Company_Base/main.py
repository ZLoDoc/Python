import imp_exp as ie
import menu
import view

def login():    
    while True:
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        
        work_data = ie.read_file("users.txt")
        for value_in_workdata in work_data:
            value = value_in_workdata.split(",")# здесь значение текущего пользователя
            if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower():
                return value
     
        print(f'Пользователь {first_name.capitalize()} {last_name.capitalize()} не обнаружен, повторите ввод')  


def modul_admin():#функцианал админ меню

    while True:
        choise_admin_menu = menu.admin_menu()
        if choise_admin_menu == "1":view.view_base("users.txt")        
        elif choise_admin_menu == "2":modul_admin_edit()
        elif choise_admin_menu == "3":menu.exit_menu()

            
def modul_admin_edit():
    choise_admin_edit_menu = menu.admin_edit_menu()
    if choise_admin_edit_menu == "1":add_users_admin()                
    elif choise_admin_edit_menu == "2": modul_admin_delete()
    elif choise_admin_edit_menu == "3":modul_admin()
        

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
        # work_data.append(result)
        # temp1 = ""
        # for value in work_data:            
        #     temp1 = temp1 + value + "\n"
        if result in work_data: 
            print('Такой пользователь есть в базе')
            return()
        else:           
            choise = input('Сохранить пользователя? Да  / Нет\n')
            if choise.lower() == "да":
                work_data.append(result)
                print (f'work_data1 = {work_data}')            
                               
                ie.write_file("users.txt", work_data )
                return()
            elif choise.lower() == "нет":
                return()


def modul_admin_delete():
    while True:
        # view.view_base("users.txt")
        choise_admin_delete_menu = menu.admin_delete_menu()
        if choise_admin_delete_menu == "1": delete_user()
        if choise_admin_delete_menu == "2": modul_admin_edit()           
            
def delete_user():
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
        
        if result not in work_data: 
            print('Такого пользователя нет в базе')
            return()
        else:            
            work_data.remove(result)
            ie.write_file("users.txt",work_data)
            view.view_base("users.txt")                        
            return()   





value = login()
print(f'Рады вас видеть {value[0]}')
if value[2] == 'admin': modul_admin()