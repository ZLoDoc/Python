import csv

def open_base():
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
             work_data = line
    return work_data


def exit(work_data):
    with open('pb.txt' , 'w') as data:
        data.writelines(work_data)


def export_txt(work_data):   
    with open('export.txt' , 'w') as data: 
        data.writelines(work_data)


def export_csv(work_data):
    with open('pb.csv', 'w', newline='') as data:#'запись'
        writer = csv.writer(work_data)
        writer.writerows(work_data)        




        # base = []
        # deep_base = []
        
        # base = work_data.split(';')   
          
        # for i in range (len(base)):                   
        #     deep_base = base[i].split(' ')        
        #     data.write(f'\n{" ".join(deep_base)}\n')

# def import_data(work_data):
#     with open('export.txt' , 'rt') as data:
#         for line in data.readlines():
#              work_data = line
#              print(work_data)
# import csv
# with open('pb.csv', 'w', newline='') as data:#'запись'
#     writer = csv.writer(data)
#     writer.writerows('someiterable')