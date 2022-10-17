# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

import random

f = open('list.txt', 'r')
sequence = list(f.read().split(' '))
f.close()

print(s1)
i = 0
# sequence = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = []
while i < (len(sequence)):
    if i == 0: 
        result_list.append(sequence[i])
        i = random.randrange(i,len(sequence)-1) #выбираю индекс второго значения        
    elif sequence[i] > result_list[(len(result_list))-1]: result_list.append(sequence[i])
    i = i + 1
result = " ".join(result_list)
print(sequence)   
print(result) 
with open('list_res.txt', 'a') as data:
    data.write(f'{" ".join(result_list)}\n')   

