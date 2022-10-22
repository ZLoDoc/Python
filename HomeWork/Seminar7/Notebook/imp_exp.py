def open_base():
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
             work_data = line
    return work_data


def exit(work_data):
    with open('pb.txt' , 'w') as data:
        data.writelines(work_data)


def export(work_data):   
    with open('export.txt' , 'w') as data: 
        base = []
        deep_base = []
        base = work_data.split(';')   
          
        for i in range (len(base)):                   
            deep_base = base[i].split(' ')        
            data.write(f'{" ".join(deep_base)}\n')
    





        