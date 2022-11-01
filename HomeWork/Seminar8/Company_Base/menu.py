import imp_exp as ie

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

# def student_menu(value):
#     print(value)
#     choise = input(' 1 - Посмотреть ДЗ\n 2 - Список оценок\n')
#     return

# def teacher_menu(value):
#     print(value)
#     choise = input(' 1 - Добавить ДЗ\n 2 - Поставить оценку\n')
#     return

# def view_menu():
#     return




