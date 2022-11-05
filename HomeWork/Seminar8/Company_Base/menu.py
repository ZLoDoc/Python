import imp_exp as ie
# import main

def login_menu(first_name, last_name):    
    
    work_data = ie.read_file("users.txt")    
    for value_in_workdata in work_data:
        value = value_in_workdata.split(",")                    
        if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower():            
            return value
   

               
def admin_menu():    
    while True:
        choise_admin_menu = str(input(' 1 - Посмотреть базу\n 2 - Редактировать базу\n 3 - Выход\n'))
        if choise_admin_menu == "1" or choise_admin_menu == "2" or choise_admin_menu == "3":
            return choise_admin_menu
        else:
            print('Ошибка ввода, повторите ввод')
            continue     
    

def admin_edit_menu():
    while True: 
        choise_admin_edit_menu = input(' 1 - Добавить пользователя\n 2 - Удалить пользователя\n 3 - Выход\n')
        if choise_admin_edit_menu == "1" or choise_admin_edit_menu == "2" or choise_admin_edit_menu == "3":
            return choise_admin_edit_menu
        else:
            print('Ошибка ввода, повторите ввод')
            continue


def admin_delete_menu():
    while True: 
        choise_admin_delete_menu = input(' 1 - Удалить пользователя\n 2 - Выход\n')
        if choise_admin_delete_menu == "1" or choise_admin_delete_menu == "2": return choise_admin_delete_menu
        else:
            print('Ошибка ввода, повторите ввод')
            continue


def role_menu():    
    while True:                         
        role = input(' 1 - админ\n 2 - преподаватель\n 3 - студент\n')
        if role == "1" or role =="2" or role =="3":            
            return role
        else:
            print('Ошибка ввода, повторите ввод')
            continue            
                       


def exit_menu():
    choise = input('Выйти? Да  / Нет\n').lower()
    if choise.lower() == "да":
        exit()
    else:
        return()

def confirm_menu():
    choise = input('Сохранить? Да  / Нет\n').lower()
    if choise.lower() == "да":
        return(True)
    else:
        return (False)

def student_menu():
   while True:
        choise_student_menu = input(' 1 - Посмотреть ДЗ\n 2 - Список сданных работ\n 3 - Выход\n')
        if choise_student_menu == "1" or choise_student_menu == "2" or choise_student_menu == "3":
            return choise_student_menu
        else:
             continue


def teacher_menu():
   while True:
        choise_student_menu = input(' 1 - посмотреть успеваимость\n 2 - посмотреть список учеников\n 3 - добавить ДЗ\n 4 - поставить оценку\n 5 - Выход\n')
        if choise_student_menu == "1" or choise_student_menu == "2" or choise_student_menu == "3" or choise_student_menu == "4" or choise_student_menu == "5":
            return choise_student_menu
        else:
             continue














