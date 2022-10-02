# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def rnd_list(n):
    rnd_lst = []
    rnd_value = 0
    for i in range(n):
        rnd_value = random.randrange(0,10)
        rnd_lst.append(rnd_value)   
    return(rnd_lst) 
    
n =  int(input('Задайте количество элементов в списке: '))
list = (rnd_list(n))
middle_index = (int(len(list)/2))
result_list = []
print(list)

for i in range (int(len(list)/2)):
    result_list.append(list[i] * (list[(len(list)-1)-i]))
if len(list)%2 != 0:
     result_list.append(list[middle_index]*list[middle_index])
print(result_list)