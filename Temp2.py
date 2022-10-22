def main_menu():
    menu_continue = 1
    while menu_continue != 0:
        choise = input(' 1 - просмотр записей\n 2 - добавление записи\n 3 - поиск\n 4 - выход    \n')
    return choise


print(main_menu())