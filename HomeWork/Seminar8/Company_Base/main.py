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
        if choise_teacher_menu == "2": 
            print('\n'.join(map(str,view.view_student_list())))
            print()
        if choise_teacher_menu == "3": add_home_work()
        if choise_teacher_menu == "4": add_mark_to_subject_teacher_sub_menu()
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



        

def add_mark_to_subject_teacher_sub_menu():

    subjects = list(view.view_subject()) #список имен предметов
    print(("--------------------------------------------------"))     
    for i, item in enumerate(subjects,1): 
        print(i," - ",item)
              
    print(("--------------------------------------------------"))    
   
    choise_subject = input(" Выберите предмет: ")    
    for j,item in enumerate(subjects,1):
        if j == int(choise_subject):
            subject = str(item)
            print(f'Домашнее задание по предмету {subject} :')
    subject_data = ie.read_file("home_work.txt") # 1,литература,выучить стихотворение пушкина
    print('-------------------------------------------')        
    
    
    
    home_work = []
    for work in subject_data:        
        if subject in work:
            home_work.append(work.split(",")[2]) #  Здесь  work = вся строка включающая имя задания ; home_work = имя задания
    for i, item in enumerate(home_work,1):
        print(i," - ",item)  
    print('-------------------------------------------')
    choise_home_work = input(" Выберите задание: ")
    for j,item in enumerate(home_work,1):
        if j == int(choise_home_work):
            home_work = str(item)
    print(home_work)
    
    for work_string in subject_data:
        if home_work in work_string:
            choise_subject = work_string.split(",")[0]
    print('-------------------------------------------')

    mark_data = ie.read_file('mark.txt') # Ли,Чан,2,4
    users = ie.read_file('users.txt') #    Ли,Чан,student
   
    user_mark_list = ""
    for j in range(len(mark_data)):
        if (mark_data[j].split(","))[2] == choise_subject:
            print(f'{(mark_data[j]).split(",")[0]} {(mark_data[j]).split(",")[1]} оценка - {(mark_data[j]).split(",")[3]}')                
            user_mark_list += ((mark_data[j]).split(",")[0]) + " " + ((mark_data[j]).split(",")[1]) +"\n" # список студентов с оценками 
     
    for n in users:            
            if  "student" in n:
                temp = n.split(",")
                if temp[0] and temp[1] in user_mark_list:
                    continue
                else: print(f'{temp[0]} {temp[1] } - не сдавал')
    print('-------------------------------------------')



    mark_student_name = input('Введите фамилию ученика : ').capitalize()
    result_list = []
    result_stydent_mark_name = ""
    for string_value in mark_data: 
        # print(string_value)       
        if mark_student_name in string_value: #проверяю что введенное имя пресутствует в списке user.txt            
            if mark_student_name not in user_mark_list: #проверяю что введенное имя не присутствует в списке студентов с оценкой
                student_mark = input('Введите оценку : ')                
                if student_mark in range(1,6): print() #проверяю что оценка в допустимом диапазоне
                result_stydent_mark_name = string_value.split(",")[0] + ',' + string_value.split(",")[1] + ',' + choise_subject.split(",")[0] + ',' + student_mark
                print(f' оценка ученика {result_stydent_mark_name}')
                result_list.append(mark_data)
                result_list.append(result_stydent_mark_name)
                ie.add_data_in_file('mark.txt',result_stydent_mark_name)
                break
  
user_list = view.view_base('users.txt')

value = login()
print(f'\nРады вас видеть {value[0]}\n')
if value[2] == 'admin': modul_admin()
if value[2] == 'student': modul_student(value)
if value[2] == 'teacher': modul_teacher()
