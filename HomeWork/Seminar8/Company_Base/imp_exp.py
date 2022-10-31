import menu
def read_file(filename):
    with open(filename , 'rt', encoding="utf-8") as data:
        line = data.readlines()
        for i in range(len(line)):
            line[i] = line[i].rstrip()        
        return line

def write_file(work_data):
    with open('pb.txt' , 'w', encoding="utf-8") as data:
        data.writelines(work_data)


def add_users_admin(work_data):    
    print(f'work_data in add_users_admin = {work_data}')
    print(f'menu.role_menu() = {menu.role_menu(work_data)}')
    # if first_name and last_name and role in work_data: 
    #     print ('Пользователь есть в базе')
    return
    
