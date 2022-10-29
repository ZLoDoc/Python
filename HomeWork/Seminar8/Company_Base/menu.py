from enum import Flag
import imp_exp as ie

def login_menu(first_name, last_name):    
    
    work_data = ie.read_file("users.txt")
    for value_in_workdata in work_data:
        value = value_in_workdata.split(",")            
        if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower(): 
            return value
               
def admin_menu(value):
    print(value)
    while
        choise = str(input(' 1 - Посмотреть базу\n 2 - Редактировать базу\n'))
        if choise == "1": 
            view_menu()
        elif choise == "2": admin_edit_menu()    
        
    return

def admin_edit_menu():
    choise = input(' 1 - Добавить пользователя\n 2 - Удалить пользователя\n')
    return

def student_menu(value):
    print(value)
    choise = input(' 1 - Посмотреть ДЗ\n 2 - Список оценок\n')
    return

def teacher_menu(value):
    print(value)
    choise = input(' 1 - Добавить ДЗ\n 2 - Поставить оценку\n')
    return

def view_menu():
    return




