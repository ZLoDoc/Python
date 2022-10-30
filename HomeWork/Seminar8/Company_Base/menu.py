import imp_exp as ie

def login_menu(first_name, last_name):    
    
    work_data = ie.read_file("users.txt")
    for value_in_workdata in work_data:
        value = value_in_workdata.split(",")            
        if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower(): 
            return value
               
def admin_menu():
    # print(value)
    while True:
        choise_admin_menu = str(input(' 1 - Посмотреть базу\n 2 - Редактировать базу\n'))
        if choise_admin_menu == "1" or "2":
            return choise_admin_menu
        
        
    

def admin_edit_menu():
    choise_admin_edit_menu = input(' 1 - Добавить пользователя\n 2 - Удалить пользователя\n')
    return choise_admin_edit_menu

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




