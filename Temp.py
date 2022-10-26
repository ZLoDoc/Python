
with open('pb.txt' , 'rt', encoding="utf-8") as data:
        for i in data.readlines():
            work_data = i
        print(f'work_data ={work_data}') 

line = ("")
with open("file_2.txt", "r", encoding="utf-8") as data:       
    for every_string in data:            
        line =  every_string.strip() + ";"
        print(f'line = {line}')          

        if line == work_data:
            with open('pb.txt' , 'w', encoding="utf-8") as data:
                data.writelines(work_data) 


        else: 
            temp = ""
            line = line.split(";")            
            work_data = work_data.split(";")            
            for x in line:
                # print(x)
                if x not in work_data:
                    temp = temp + x + ";"
            work_data = ";".join(work_data)
            work_data += temp              
                
            with open('pb.txt' , 'w', encoding="utf-8") as data:
                data.writelines(work_data)
            


# def import2_txt(): рабочий код 
#     work_data = ""
#     with open("file_2.txt", "r", encoding="utf-8") as data:       
#         for line in data:            
#             work_data = work_data + line.strip() + ";"
#             with open('pb.txt' , 'w', encoding="utf-8") as data:
#                 data.writelines(work_data)
#     return work_data






      