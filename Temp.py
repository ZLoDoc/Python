import imp_exp as ie
def add_home_work():
    home_work_data = ie.read_file('home_work.txt')
    subject = input('введите название предмета')
    home_work = input('Напишите ДЗ')
    print (home_work_data)
    print(subject)
    print(home_work)

add_home_work()