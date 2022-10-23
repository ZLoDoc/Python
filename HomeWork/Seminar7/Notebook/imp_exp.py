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
        data.writelines(work_data)
        data.write('\n#######')

        base = []
        deep_base = []
        
        base = work_data.split(';')   
          
        for i in range (len(base)):                   
            deep_base = base[i].split(' ')        
            data.write(f'\n{" ".join(deep_base)}\n')

# def import_data(work_data):
#     with open('export.txt' , 'rt') as data:
#         for line in data.readlines():
#              work_data = line
#              print(work_data)

def create_csv(filename="new_export"):
    with open('database.csv', "rb") as data:
        with open(f"export/{filename}.csv", "wb") as new_file:
            new_file.writelines(data.readlines())


def csv_import(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        for row in reader:
            add_note(row["Фамилия"], row["Имя"], row["Телефон"], row["Описание"])
            counter += 1
    print(f"Импортировано записей: {counter}")