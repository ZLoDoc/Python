# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# изначальный вариант

# def rnd_list(n):
#     rnd_lst = []
#     rnd_value = 0
#     for i in range(n):
#         rnd_value = random.randrange(0,10)
#         rnd_lst.append(rnd_value)    
#     return(rnd_lst) 
   

# n =  int(input('Задайте количество элементов в списке: '))
# rnd_lst = (rnd_list(n))
# print(rnd_lst)
# result = 0
# for i in range(len(rnd_lst)):
#     if i%2 != 0:
#         result += rnd_lst[i]
#         print(f'list[{i}] = {rnd_lst[i]}')
# print(f'Сумма всех элементов стоящих на не четных позициях = {result}')
# ---------------------------------------------------------------------------------

# вариант с enumerate и List comprehension

def rnd_list(n): # генерация случайного списка
    rnd_lst = []
    rnd_value = 0
    for i in range(n):
        rnd_value = random.randrange(0,10)
        rnd_lst.append(rnd_value)    
    return(rnd_lst)



def sum_of_odd_index(n):   #вариант 1  
    
    sum = 0
    for i, num in enumerate(n):
        if not i % 2: 
            sum+=num

    print(n)            
    print (f' ответ вариант 1 : {sum}')
       
    # другой вариант    

def sum_of_odd_index2(n):     #Вариант2 

    result = sum(n[x] for x in range(len(n)) if x % 2 == 0)        
    
    print(n)
    print(f' ответ вариант 2 : {result}')




n = rnd_list(int(input('Задайте количество элементов в списке: ')))
sum_of_odd_index(n)
sum_of_odd_index2(n)