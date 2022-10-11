# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# 1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
import re
  
num = input('Введите ряд чисел: ')
num = (re.split(" ,|, | |;|,|\n", num))
# for i in range(len(num)):
count = 0
res_list=[]
for i in range(len(num)):
    print(f'num i{i} = {num[i]}')
    for j in range(len(num)):
        if num[j]==num[i]:
            count = count + 1
    if count == 1:
        res_list.append(num[i])

    # print(f'num i{i} = {num[i]}')
        print(f'   num j{j} = {num[j]}')
        print('----------------------------')
    
    # print('----------------------------')
#         if num[i] == num[j]:
#             count = count+1
#     if count == 1:
#         result = result + num[i]