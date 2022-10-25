def export2_txt():
    result=""   
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
            work_data = line.strip()
            
            print(work_data.split(";"))
            for i in work_data.split(";"):
                print(work_data)
           
                
            

    # with open('file_2.txt' , 'w') as data:
    #     data.writelines(result)
    # print(result)

export2_txt()