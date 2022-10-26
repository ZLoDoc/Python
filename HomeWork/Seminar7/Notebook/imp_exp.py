def open_base():
    with open('pb.txt' , 'rt', encoding="utf-8") as data:
        for line in data.readlines():
             work_data = line
    return work_data


def exit(work_data):
    with open('pb.txt' , 'w', encoding="utf-8") as data:
        data.writelines(work_data)


def export1_txt(work_data):   
    with open('file_1.txt' , 'w', encoding="utf-8") as data: 
        data.writelines(work_data)


def export2_txt(work_data):
    result=""   
    with open('pb.txt' , 'rt', encoding="utf-8") as data:
        for line in data.readlines():
            work_data = line.split(";")

        for i in work_data:
             if i != "":
                result = result + (f'{i}\n')    

    with open('file_2.txt' , 'w', encoding="utf-8") as data:
        data.writelines(result)


# def import1_txt(): рабочий код
#     with open('file_1.txt' , 'rt', encoding="utf-8") as data:
#         for line in data.readlines():
#              work_data = line             
#     with open('pb.txt' , 'w', encoding="utf-8") as data:
#         data.writelines(work_data)
#     return work_data

def import2_txt():
    work_data = ""
    with open("file_2.txt", "r", encoding="utf-8") as data:       
        for line in data:            
            work_data = work_data + line.strip() + ";"
            with open('pb.txt' , 'w', encoding="utf-8") as data:
                data.writelines(work_data)
    return work_data



def import1_txt(work_data):#добавляет только новые записи
    with open('pb.txt' , 'rt', encoding="utf-8") as data:
        for line in data.readlines():
             work_data = line        

    with open('file_1.txt' , 'rt', encoding="utf-8") as data:
        for line in data.readlines():          

            if line == work_data:
                with open('pb.txt' , 'w', encoding="utf-8") as data:
                    data.writelines(work_data)
            
            else: 
                temp = ""
                line = line.split(";")            
                work_data=work_data.split(";")            
                for x in line:
                    print(x)
                    if x not in work_data:
                        temp = temp + x + ";"
                work_data = ";".join(work_data)
                work_data+=temp
                print(f'temp = {temp}')    
                print(f'work_data = {work_data}')
                return work_data