# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

import random
i = 0
sequence = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = []
while i < (len(sequence)):
    if i == 0: 
        result_list.append(sequence[i])
        i = random.randrange(i,len(sequence)) #выбираю индекс второго значения
        print(i)
    elif sequence[i] > result_list[(len(result_list))-1]: result_list.append(sequence[i])
    i = i + 1
print(result_list)    

