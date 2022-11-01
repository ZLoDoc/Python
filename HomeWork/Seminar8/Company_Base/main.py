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
                return value
     
        print(f'Пользователь {first_name.capitalize()} {last_name.capitalize()} не обнаружен, повторите ввод')
        value = "bad_input"            
            
def add_users_admin():
    while True:
        work_data = ie.read_file("users.txt")    
        print(f'work_data in add_users_admin = {work_data}')
        result = str("")
        first_name = input('Введите имя: ')
        result += first_name.capitalize()
        last_name = input('Введите фамилию: ')
        result += "," + last_name.capitalize()
        print('Задайте роль : ')
        role =  menu.role_menu()
        if role == "1": role = "admin"
        if role == "2": role = "teacher"
        if role == "3": role = "student"
        result += "," + role
        work_data.append(result)
        print(work_data)

        choise = input('Сохранить пользователя? Да  / Нет\n')
        if choise.lower() == "да":             
            temp=""
            for item in work_data:
                temp = temp + (f'{item}\n')
                ie.write_file("users.txt", temp)
                return()
        elif choise.lower() == "нет":
            return()
                              


   


def modul_admin():#функцианал админ меню
    print(f'value = {value}')
    while True:
        choise_admin_menu = menu.admin_menu(ie.read_file("users.txt"))
        if choise_admin_menu == "1":
            view.view_base(ie.read_file("users.txt"))
        elif choise_admin_menu == "3":
            menu.exit_menu()
        elif choise_admin_menu == "2":

            choise_admin_edit_menu = menu.admin_edit_menu()
            if choise_admin_edit_menu == "1":
                add_users_admin()
                b = menu.role_menu()
                # print(work_data)





            elif choise_admin_edit_menu == "2": print('Удаляем пользователя')


        # if value[2] == 'student':
        #     choise = menu.student_menu(value)
        # if value[2] == 'teacher':
        #     choise = menu.teacher_menu(value)
        # print(choise)

value = login()
print(f'Рады вас видеть {value[0]}')
if value[2] == 'admin': modul_admin()