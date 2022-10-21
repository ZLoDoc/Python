with open('pb.txt' , 'rt') as data: # автоматически закрывает файл
    
# data.readlines()
    for line in data.readlines():
         work_data = line
         print(line)
print(work_data.split(";"))
a = work_data.split(";")
print(f'a = {a[0]}')
print(type(work_data))
