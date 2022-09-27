# Пример ветвления
# a = 5
# b = 15
# c = a * b
# if a > 5:
#     c = c * 2
# if a > 9: - будет проверят, даже если выполнился верхний if
#     c = c * 2
# elif: - не будет проверят если выполнился if
#     c = c * 3    
# print(c)

# #Пример цикла For
# n=int(input())
# sum_=0
# for i in range(n):
#     number = int(input())
#     sum_+=number
# print(sum_/n)    

# #Пимер цикла While
# number = int(input())
# cnt = 0
# sum_ = 0
# while number != 0:
#     sum_+=1
#     number=int(input())
#     print(sum_/cnt)

#break - останавливает цикл
#continue - переходит к следующей итерации(переходит к условию цикла )

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# else:
#     print('Цикл завершился штатно ') #-выполняется только если for завершился     


#range(start,stop,step)
# range (1,20,5) - 1,6,11,16

#ФУНКЦИИ
# def f():
#     print('Как вас зовут')
#     name = input()
#     print (f'Здравствуйте {name}')

# f()
#-----------------------------

# def f_x(x,y,r):
#     return x**2+15*y-r
#     #после ретурна ничего не выполняется
# y=f_x(35,22,44)
# print('y =',y)
#-------------------------------
# def f(a:list,b):
#     return int(len(a)/b)

# print(f([1,2,3,4,5,6],6))

#СПИСКИ

# str_ = 'qwer, dfdfdf, erwrer, werewrm'
# print(str_.split(', '))
# print(dir(str_)) # dir выводит все возможные методы

# print(help(str.isalpha))
#print(__name__)