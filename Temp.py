with open('pb.txt' , 'rt') as data:
        for line in data.readlines():
             work_data = line
# output_list = []             
with open('export.txt' , 'w') as data: 
    base = []
    deep_base = []
    base = work_data.split(';')   
          
    for i in range (len(base)):                   
        deep_base = base[i].split(' ')        
        data.write(f'{" ".join(deep_base)}\n')   


                       
        # deep_base = deep_base.join(base[i].split(' '))
        # print(deep_base)
        # data.write(f'{deep_base}\n')