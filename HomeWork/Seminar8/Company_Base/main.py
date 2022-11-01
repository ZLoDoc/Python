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

def modul_student(value):
    while True:
        choise_student_menu = menu.student_menu()
        if choise_student_menu == "1": view_home_work(value) # показать только задания залогиневшегося студента
        if choise_student_menu == "2": view_mark(value)
        if choise_student_menu == "3": menu.exit_menu()    

def view_home_work(value):#< -------Исключить оцененные ДЗ из списка
    result = ""
    home_work_data = ie.read_file('home_work.txt')
    mark_data = ie.read_file('mark.txt')

    for i in range (len(mark_data)):
        if (value[0] and value[1]) in str(mark_data[i]).split(","):


            # for j in range(len(home_work_data)):
            #     if(home_work_data[j]).split(",")[0] != (mark_data[i]).split(",")[2]:
            #         if home_work_data[j] not in result:
            #             result += (home_work_data[j]).split(",")[1]+((home_work_data[j]).split(",")[2])
            #             print(result)
    


def view_mark(value):
    
    mark_data = ie.read_file('mark.txt')
    home_work_data = ie.read_file('home_work.txt')

    for i in range (len(mark_data)):
        if (value[0] and value[1]) in str(mark_data[i]).split(","):             
            for j in range(len(home_work_data)):
                if (mark_data[i]).split(",")[2] == (home_work_data[j]).split(",")[0]:
                    print(f'Оценки ученика {value[0]} {value[1]} по предмету {(home_work_data[j]).split(",")[1]} за работу " {(home_work_data[j]).split(",")[2]}" - {(mark_data[i]).split(",")[3]} балла')
                    
   

value = login()
print(f'Рады вас видеть {value[0]}')
if value[2] == 'admin': modul_admin()
if value[2] == 'student': modul_student(value)