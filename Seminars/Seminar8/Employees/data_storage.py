# База пользователя

def data_read(id, filename):
    with open (filename, "r", "") as file:
        lines = file.readlines()
        if len(lines) == 0:
            return 1
        else:
                
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
    temp_output = ""
    with open (filename, "r", "") as file:
        lines = file.readlines()
        if len(lines) == 0 or id > 5 or id < 0:
            print('Данные отсутствуют в таблице')
            return 1
        else:
            for line in lines:
                if id in line:
                    line_data = str(line).split(";")  
                    if par < 0 or par >= len(line_data):
                        return -1
                    line_data[par] = value

                    for i in line_data:
                        temp_output = f"{temp_output}{i}"
                                                            
                    with open(filename, "w", "") as file:
                        for i in lines:
                            if i != line:
                                file.write(i)
                            else:
                                file.write(f"{temp_output}\n")
                                return temp_output


                print('Данные отсутствуют в таблице')
                return -1
        