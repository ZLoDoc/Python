import imp_exp as ie
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
                    
                    print(f'{((home_work_data[j]).split(",")[1]).capitalize()} за работу - "{(home_work_data[j]).split(",")[2]}" - {(mark_data[i]).split(",")[3]} балла')
                    
    print()