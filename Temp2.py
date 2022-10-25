def export2_txt():
    result=""
    a=[]  
    with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
            work_data = line                       
            result=(work_data.split(";"))
            for i in result:
                print(i)
           
                
            

    # with open('file_2.txt' , 'w') as data:
    #     data.writelines(result)
    # print(result)

export2_txt()