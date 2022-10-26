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