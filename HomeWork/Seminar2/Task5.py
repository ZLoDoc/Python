# 5. Реализуйте алгоритм перемешивания списка.
# random.randint(2, 6)
# random.randrange(2, 6)
# '''
import random

stroka=list(input(f'Введите список : '))
print(stroka)
for i in range (100):
    index_1 = random.randrange(len(stroka))
    index_2 = random.randrange(len(stroka))
    temp = stroka[index_1]
    stroka[index_1]=stroka[index_2]
    stroka[index_2]=temp
print(stroka)


