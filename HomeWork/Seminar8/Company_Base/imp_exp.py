# import menu

def read_file(filename):
    with open(filename, 'rt', encoding="utf-8") as data:
        line = data.readlines()
        for i in range(len(line)):
            line[i] = line[i].rstrip()        
        return line


def write_file(filename, work_data):# work_data должна быть в list   
    temp = ""
    for value in work_data:
        temp = temp + value + "\n"
    print(temp)
    with open( filename, 'w', encoding="utf-8") as data:
        data.writelines(temp)


def add_data_in_file(filename, work_data):  
    with open( filename, 'a', encoding="utf-8") as data:
        data.writelines(f'\n{work_data}')