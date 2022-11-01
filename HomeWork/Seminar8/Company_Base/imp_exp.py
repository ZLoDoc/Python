import menu
def read_file(filename):
    with open(filename, 'rt', encoding="utf-8") as data:
        line = data.readlines()
        for i in range(len(line)):
            line[i] = line[i].rstrip()        
        return line

# def write_file(filename, work_data):
#     with open(filename, 'w', encoding="utf-8") as data:
#         data.writelines(work_data)


def write_file(filename, work_data):  # добавляет уникальные записи
    print(work_data)  
    # with open(filename, 'rt', encoding="utf-8") as data:
    #     for work_data in data.readlines():            
            # result = result + (f'{work_data}')            
    with open(filename, 'w', encoding="utf-8") as data:
        data.writelines(work_data)

