# import imp_exp as ie
import menu

def login():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    value = menu.login_menu(first_name, last_name)    
    return value    

def modul_admin():
        choise_admin_menu = menu.admin_menu()
        if choise_admin_menu == 1 : print('Смотрим базу пользователей')
        elif choise_admin_menu == 2:
            choise_admin_edit_menu = menu.admin_edit_menu()
            if choise_admin_edit_menu == 1: print('Добавляем пользователя')
            elif choise_admin_edit_menu == 2: print('Удаляем пользователя')


        # if value[2] == 'student':
        #     choise = menu.student_menu(value)
        # if value[2] == 'teacher':
        #     choise = menu.teacher_menu(value)
        # print(choise)

value = login()
if value[2] == 'admin': modul_admin()