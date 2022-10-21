# База пользователя

def data_read(id, filename):
    with open (filename, "r", "") as file:
        lines = file.readlines()
        if len(lines) == 0:
            return 1
        else:
            for line in lines:
                if id in line:
                    line_data = str(line).split(";")
                    login = line_data[0]
                    password = line_data[1]
                    familie = line_data[2]
                    name = line_data[3]
                    status = line_data[4]
                    description = line_data[5]
                    return login, password, familie, name, status, description
                print('Данные отсутствуют в таблице')
                return -1

def data_write(id, filename, value, par):
    with open (filename, "r", "") as file:
        lines = file.readlines()
        if len(lines) == 0 or id > 5 or id < 0:
            print('Данные отсутствуют в таблице')
            return 1
        else:
            for line in lines:
                if id in line:
                    line_data = str(line).split(";")
                    login = line_data[0]
                    password = line_data[1]
                    familie = line_data[2]
                    name= line_data[3]
                    status = line_data[4]
                    description = line_data[5]
                    if par == 0:
                        login = value
                    if par == 1:
                        password = value
                    if par == 2:
                        familie = value
                    if par == 3:
                        name = value
                    if par == 4:
                        status = value
                    if par == 5:
                        description = value
                    temp_string = (f"{login};{password};{familie};{name};{status};{description};")
                    
                with open(filename, "w", "") as file:
                    for i in lines:
                        if i != line:
                            file.write(i)
                        else:
                            file.write(f"{temp_string}\n")
                            return temp_string


                print('Данные отсутствуют в таблице')
                return -1
        