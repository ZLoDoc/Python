# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# 1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
  
num = input('Введите ряд чисел: ')
result = []
for i in range(len(num)):
    count = 1   
    for j in range(len(num)):
        if num[i] == num[j] and i != j:
            count = 0
            break
    if count == 1:
        result.append(num[i])
print(f'Список неповторяющихся элементов -  {result}')