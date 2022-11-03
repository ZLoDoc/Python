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
        if choise_teacher_menu == "2": view.view_student_list()
        if choise_teacher_menu == "3": add_home_work()
        if choise_teacher_menu == "4": add_mark()
        if choise_teacher_menu == "5": menu.exit_menu()

def add_home_work():    
    home_work_data = ie.read_file('home_work.txt')
    for lesson_string in home_work_data:
        subject = lesson_string.split(",")[1] + " - " + lesson_string.split(",")[2]    
        print(subject)
    
    temp = ""
    temp = str(len(home_work_data)+1) + ","    
    subject = input('введите название предмета: ')
    home_work = input('Напишите ДЗ: ')
    temp += (subject) + "," + (home_work)
    print(temp)
    home_work_data.append(temp)
    if menu.confirm_menu():
        ie.write_file('home_work.txt',home_work_data)

def add_mark(): 
     
    # view.view_teacher_mark()
    students = list(view.view_student_list())
    print(f' Это именно тот students{students}')
    subjects = list(view.view_subject())    
    print("--------------------------------------------------")
    for i, item in enumerate(students,1): 
        print(i," - ",item)
    print(("--------------------------------------------------"))    
    for i, item in enumerate(subjects,1): 
        print(i," - ",item)        
    print(("--------------------------------------------------"))    
    
    choise_subject = input(" Выберите предмет: ")
    for j,item in enumerate(subjects,1):
        if j == int(choise_subject):
            subject = str(item)

    choise_student = input(" Выберите студента: ")
    for j,item in enumerate(students,1):
        if j == int(choise_student):
            student = str(item)            

    print(f'предмет - {subject}')
    print(f'студент - {student}')

    mark_data = ie.read_file("mark.txt")    
    subject_data = ie.read_file("home_work.txt")    
    work_result = "" 

    print('-------------------------------------------')
    for work in subject_data:
        if subject in work:
            work_result = (work.split(",")[1]) + "," + (work.split(",")[2])
            
            print('несданные задания:')
            print(work_result)  
    print('-------------------------------------------') 
    
    print('-------------------------------------------')
    for persons in mark_data:
        print(f'student - {student} in persons {persons}')
        
        
        if student in persons:
            print(persons)
            person_result = (persons.split(",")[0]) + "," + (persons.split(",")[1])            
            print('студент найден:')
            print(person_result)  
    print('-------------------------------------------')                      







    
   

value = login()
print(f'\nРады вас видеть {value[0]}\n')
if value[2] == 'admin': modul_admin()
if value[2] == 'student': modul_student(value)
if value[2] == 'teacher': modul_teacher()
