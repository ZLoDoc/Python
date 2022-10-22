def find_value(work_data):
    find_result = ''
    find = input('Введите искомое значение: ')
    base = []
    deep_base = []
    find_result = []
    base = work_data.split(';')   
            
    for i in range (len(base)):
        print(f'i{i} = {base[i]}')                
        deep_base = base[i].split(' ')

        for j in range (len(deep_base)):
                    
            print(f'deepbase[{j}] = {deep_base[j]}')
            if deep_base[j] == find:
                find_result.append(base[i])
                        
            print(f'\nИскомая запись\n')
            for i in range(len(find_result)):
                print(find_result[i])
            print()