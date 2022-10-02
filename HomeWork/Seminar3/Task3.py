# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def rnd_list(n):
    rnd_lst = []
    rnd_value = 0
    for i in range(n):
        rnd_value = round(random.randrange(0,10) + random.random(),2)
        rnd_lst.append(rnd_value)   
    return(rnd_lst) 
    
n =  int(input('Задайте количество элементов в списке: '))
list = (rnd_list(n))
print(list)
min_value = list[1]
max_value = 0
for i in range(len(list)):
    list[i] = round((list[i]%1),2)
    if min_value > list[i]:
        min_value = list[i]
    elif max_value < list[i]:
        max_value = list[i]
print(f'Минимальное значение после запятой : {min_value}')
print(f'Максимальное значение после запятой : {max_value}')
print(f'Pазница между максимальным и минимальным значением дробной части : {round(max_value - min_value,2)}')