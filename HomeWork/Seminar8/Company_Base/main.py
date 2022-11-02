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
        if choise_student_menu == "1": view.view_home_work(value)
        if choise_student_menu == "2": view.view_mark(value)
        if choise_student_menu == "3": menu.exit_menu()    

def modul_teacher():
     while True:        
        choise_teacher_menu = menu.teacher_menu()
        if choise_teacher_menu == "1": view.view_teacher_mark()
        if choise_teacher_menu == "2": print("Нужно добавить ДЗ")
        if choise_teacher_menu == "3": print("Нужно ставить оценку")
        if choise_teacher_menu == "4": menu.exit_menu()

def add_home_work():
    home_work_data = ie.read_file('home_work.txt')
    subject = list(input('введите название предмета: '))
    home_work = list(input('Напишите ДЗ: '))
    home_work_data.append(subject).split(",")
    home_work_data.append(home_work)
    print (home_work_data)



    
   

value = login()
print(f'\nРады вас видеть {value[0]}\n')
if value[2] == 'admin': modul_admin()
if value[2] == 'student': modul_student(value)
if value[2] == 'teacher': modul_teacher()
# add_home_work()