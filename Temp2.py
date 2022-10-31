def role_menu():
    with open("users.txt" , 'rt', encoding="utf-8") as data:
        line = data.readlines()
            
    result = str("")
    first_name = input('Введите имя: ')
    result += first_name
    last_name = input('Введите фамилию: ')
    result += "," + last_name
    print('Задайте роль : ')
    role = input(' 1 - админ\n 2 - преподаватель\n 3 - студент\n')
    if role == "1": role = "admin"
    if role == "2": role = "teacher"
    if role == "3": role = "student"
    result += "," + role
    line.append(result)
    print(line)
    return()

role_menu()    