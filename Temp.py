from fileinput import close


# def import2_txt():
work_data = ""
with open("file_2.txt", "r") as data:       
    for line in data:            
        work_data = work_data + line.strip() + ";"            
    print(work_data)
with open('pb.txt' , 'w') as data:
    data.writelines(work_data)            
    