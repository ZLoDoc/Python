import imp_exp as ie

# print(",\n".join(map(str, home_work_data)))

def view_base(filename):

    work_data =  ie.read_file(filename)    
       
    print() 
    for value in work_data:
        print(f'{value}')
    print()            



def view_home_work(value):
    
    subject_with_mark = ""
    temp =[]
    result = []
    home_work_data = ie.read_file('home_work.txt')
    mark_data = ie.read_file('mark.txt')

    for i in range (len(mark_data)):
        if (value[0] and value[1]) in str(mark_data[i]).split(","):


            for j in range(len(home_work_data)):
                if(home_work_data[j]).split(",")[0] == (mark_data[i]).split(",")[2]:
                    subject_with_mark = subject_with_mark + str(home_work_data[j]) + "\n"
                    temp = subject_with_mark.split("\n")

    result = [item for item in home_work_data if item not in temp]
    
    print(f'\n')
    print('Не сданные работы:')
    for value in result:
        print(f'{value[2:]}')
    print(f'\n')           



def view_mark(value):
    
    mark_data = ie.read_file('mark.txt')
    home_work_data = ie.read_file('home_work.txt')

    print()
    for i in range (len(mark_data)):
        if (value[0] and value[1]) in str(mark_data[i]).split(","):             
            for j in range(len(home_work_data)):
                if (mark_data[i]).split(",")[2] == (home_work_data[j]).split(",")[0]:
                    
                    print(f'{((home_work_data[j]).split(",")[1]).capitalize()}, за работу - "{(home_work_data[j]).split(",")[2]}" - {(mark_data[i]).split(",")[3]} балла')
                    
    print()

def view_teacher_mark():
    home_work_data = ie.read_file('home_work.txt')
    mark_data = ie.read_file('mark.txt')
    users = ie.read_file('users.txt')
    user_mark_list = []
    temp = ""
    for i in range(len(home_work_data)):
        value_in_cukle = i
        temp = ""
        # temp = (mark_data[j]).split(",")[0] + (mark_data[j]).split(",")[1]
        print('-------------------------------')        
        print(f'{(home_work_data[i].split(","))[1]} - {(home_work_data[i].split(","))[2]}')
        for j in range(len(mark_data)-1):
            if (mark_data[j].split(","))[2] == (home_work_data[i].split(","))[0]:
                print(f'\t\t{(mark_data[j]).split(",")[0]} {(mark_data[j]).split(",")[1]} оценка - {(mark_data[j]).split(",")[3]}') 
        print('-------------------------------')     
        
def view_student_list():
    work_data =  ie.read_file('users.txt')           
    print()     
    for value in work_data:
        if value.split(",")[2]=='student': print(f'{value}')
    print() 

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # for j in range(len(mark_data)-1):            
        #     if (mark_data[j].split(","))[2] == (home_work_data[i].split(","))[0]:
        #         user_mark_list.append((mark_data[j]).split(",")[0])
        #         user_mark_list.append((mark_data[j]).split(",")[1])
        #         user_mark_list.append(";")
        #         temp = "".join(user_mark_list)
        # print(f'user_mark_list = {user_mark_list}')
        # print(temp)
            # print(f'\t\t{(mark_data[j]).split(",")[0]} {(mark_data[j]).split(",")[1]} оценка - {(mark_data[j]).split(",")[3]}')
        
        # for n in range(len(mark_data)-1):
        #     if((mark_data[n].split(","))[2] != (home_work_data[i].split(","))[0]):
        #         if((mark_data[n].split(","))[0]) and ((mark_data[n].split(","))[1]) not in temp :
        #             print(f'\t\t{(mark_data[n]).split(",")[0]} {(mark_data[n]).split(",")[1]} - не сдавал  '  )

            




                       
            
    #         # elif(mark_data[j].split(","))[2] != (home_work_data[i].split(","))[0]:
    #             # print(f'\t\t{(mark_data[j]).split(",")[0]} {(mark_data[j]).split(",")[1]} - не сдавал  '  ) 
    # # print(f'temp = {temp}')

# view_teacher_mark()