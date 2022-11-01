import imp_exp as ie
def view_base(filename):    
    work_data =  ie.read_file(filename)    
    print() 
    for value in work_data:
        print(f'{value}')
    print()            