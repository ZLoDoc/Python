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
    for i in range(len(home_work_data)):
        print('-------------------------------')        
        print(f'{(home_work_data[i].split(","))[1]} - {(home_work_data[i].split(","))[2]}')

        user_mark_list = ""
        for j in range(len(mark_data)):
            if (mark_data[j].split(","))[2] == (home_work_data[i].split(","))[0]:
                print(f'\t\t{(mark_data[j]).split(",")[0]} {(mark_data[j]).split(",")[1]} оценка - {(mark_data[j]).split(",")[3]}')                
                user_mark_list += ((mark_data[j]).split(",")[0]) + " " + ((mark_data[j]).split(",")[1]) +"\n"                          
            
        for n in users:            
            if  "student" in n:
                temp = n.split(",")
                if temp[0] and temp[1] in user_mark_list:
                    continue
                else: print(f'\t\t{temp[0]} {temp[1] } - не сдавал')
            
    print('-------------------------------')           
        
def view_student_list():
    students_list = []
    students = ""
    work_data = ie.read_file('users.txt')
    print()     
    for value in work_data:
        if value.split(",")[2] == 'student':
            # print(f'{value.split(",")[0]} {value.split(",")[1]}')
            students += (value.split(",")[0]) + "," + (value.split(",")[1])
            students_list.append(((value).split(",")[0]) + "," + (value.split(",")[1]))
            print()
    
    # print(students)
    # print(students_list)
    return (students_list)




def view_subject():    
    temp_list = []
    subjects_list = []
    work_data = ie.read_file("home_work.txt")    
    for string in work_data:
        subjects_list.append(string.split(',')[1])

    for i in subjects_list:
        if i in temp_list:
            continue
        else:
            temp_list.append((i))         
    return (temp_list)







# view_subject() 

