import imp_exp as ie

def login_menu(first_name, last_name):    
    
    work_data = ie.read_file("users.txt")
    print(f'work_data in login menu{work_data}')
    for value_in_workdata in work_data:
        value = value_in_workdata.split(",")
        print(f'value in login_menu = {value}')            
        if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower():
            print(f'value in login_menu = {value}')        
            return value
   

               
def admin_menu(work_data):
    print(work_data)
    while True:
        choise_admin_menu = str(input(' 1 - Посмотреть базу\n 2 - Редактировать базу\n 3 - Выход\n'))
        if choise_admin_menu == "1" or "2":
            return choise_admin_menu
        
        
    

def admin_edit_menu():
    while True: 
        choise_admin_edit_menu = input(' 1 - Добавить пользователя\n 2 - Удалить пользователя\n 3 - Выход\n')
        return choise_admin_edit_menu

def role_menu():
    
    while True:                         
        role = input(' 1 - админ\n 2 - преподаватель\n 3 - студент\n')            
        return(role)

def exit_menu():
    choise = input('Выйти? Да  / Нет\n').lower()
    if choise == "Да": 
        exit
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




