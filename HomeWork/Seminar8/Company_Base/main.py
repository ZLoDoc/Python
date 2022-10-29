from unicodedata import name
import imp_exp as ie
import menu

def login():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    value = menu.login_menu(first_name, last_name)
    print (value)
    if value[2] == 'admin': menu.admin_menu(value)
    if value[2] == 'student': menu.student_menu(value)
    if value[2] == 'teacher': menu.teacher_menu(value)

login()