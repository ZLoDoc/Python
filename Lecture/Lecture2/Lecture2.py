
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# # data.writelines(colors)     # разделителей не будет
# data.writelines('LINE2\n')
# data.write('LINE3\n')
# data.close()

# exit()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
 
#  Функции и модули

#   def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# файл hello.py содержит следующий код
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# import hello
# print(hello.f(2.3))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...
#
# Кортеж - не изменяемый список
#
# a = (3,4,41,5)
# print(a)
# print(a[0]) # 3
# print(a[-2]) # 41 - второй элемент с конца
# a[0] = 12 # ошибка!!! Кортеж не изменяется

# print(type(a))
# x = a[0]
# print(type(x))
# b = [3,4]
# print(b)
# print(type(b))
# y = b[0]
# print(type(y))

# a=(1,2,3)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# # t[0] = 'black' # TypeError: 'tuple' object does not support item assignment 

# t = tuple(['red', 'green', 'blue']) #список превращаем в кортеж
# print(t)
# print(type(t))
# red, green, blue = t #переменным присваиваем значения хранящиеся в кортеже
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue
# print(type(red))

# dictionary = {}
# dictionary = \
# {
# 'up': '↑',
# 'left': '←',
# 'down': '↓',
# 'right': '→'
# }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

# # print(dictionary['left']) # ←
# # # типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)

# Множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}


