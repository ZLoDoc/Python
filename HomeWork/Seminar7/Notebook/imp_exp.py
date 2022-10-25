import csv

def open_base():
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
             work_data = line
    return work_data


def exit(work_data):
    with open('pb.txt' , 'w') as data:
        data.writelines(work_data)


def export1_txt(work_data):   
    with open('file_1.txt' , 'w') as data: 
        data.writelines(work_data)




def export2_txt(work_data):
    result=""   
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
            work_data = line    
    for i in work_data.split(';'): 
        result += i + ('\n')
        print(f'result={result}')    

    with open('file_2.txt' , 'w') as data:
        data.writelines(result)





def import1_txt():
    with open('file_1.txt' , 'rt') as data:
        for line in data.readlines():
             work_data = line
    with open('pb.txt' , 'w') as data:
        data.writelines(work_data)

    return work_data

def import2_txt():
    work_data = ""
    with open("file_2.txt", "r") as data:       
        for line in data:            
            work_data = work_data + line.strip() + ";"            
    # print(work_data)
    with open('pb.txt' , 'w') as data:
        data.writelines(work_data)        
    return work_data
