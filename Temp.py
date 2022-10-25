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
            for i in work_data.split(";"):
                for j in line.split(";"):
                    if j == i: continue
                    else: temp = temp + j
            work_data += temp         
print(f'work_data={work_data}')
print (f'line={line}')
print (f'temp={temp}')