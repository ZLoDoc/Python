import imp_exp as ie
import menu
import view

def login():
    # a = 1
    while True:
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        work_data = ie.read_file("users.txt")
        for value_in_workdata in work_data:
            value = value_in_workdata.split(",")# здесь значение текущего пользователя
            if first_name.lower() == value[0].lower() and last_name.lower() == value[1].lower():
                print(f'value in login = {value}')
                a = 0
                return value
     
        print(f'Пользователь {first_name.capitalize()} {last_name.capitalize()} не обнаружен, повторите ввод')
        value = "bad_input"            
            

def modul_admin():#функцианал админ меню
    print(f'value = {value}')
    while True:
        choise_admin_menu = menu.admin_menu(ie.read_file("users.txt"))
        if choise_admin_menu == "1" : view.view_base(ie.read_file("users.txt"))
        elif choise_admin_menu == "3": menu.exit_menu()
        elif choise_admin_menu == "2":            
            choise_admin_edit_menu = menu.admin_edit_menu()
            if choise_admin_edit_menu == "1":

                a = ie.add_users_admin((ie.read_file("users.txt")))
                print(f'a={a}')
            elif choise_admin_edit_menu == "2": print('Удаляем пользователя')


        # if value[2] == 'student':
        #     choise = menu.student_menu(value)
        # if value[2] == 'teacher':
        #     choise = menu.teacher_menu(value)
        # print(choise)

value = login()
print(f'Рады вас видеть {value[0]}')
if value[2] == 'admin': modul_admin()