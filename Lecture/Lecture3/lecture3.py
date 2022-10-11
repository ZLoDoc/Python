# Лямбда 
# ___________________________________________________
# def sum (x,y):     # Функция 1 тождественна lambda
#     return x+y

# sum = lambda x, y: x+y    # lambda тождественна функция 1  

 # def mylt(x, y):
#     return x*y


# def calc(op,a,b):
#     print(op(a,b))

# calc(sum, 5, 4)

# -------------------------------------------------

# def calc(op,a,b):
#     print(op(a,b))

# calc(lambda x, y: x+y, 5, 4)
 

 # List Comprehension
 # ___________________________________________________________________ 

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]
# ------------------------------------
# list = []
# for i in range (1,101):                                               
#     if (i%2 ==0):
#         list.append(i)
# ______________________________________

# def f(x):
#     return x**3

# list = [f(i) for i in range (1,21) if i%2 == 0]
# _____________________________________________________


# f = open('new_file', 'r')
# data = f.read() + ' ' #читаем строку и добавляем в конце пробел
# f.close()
# # print(data)

# numbers = []

# while data != '': # Выполняем пока не появится пустой элемент
#     space_pos = data.index(' ') # Находим первую позицию пробела
#     numbers.append(int(data[:space_pos])) # Выбираем все что находится от первого символа до первого пробела и превратить в число
#     data = data[space_pos+1:]
#     print(numbers)


# out = [(i,i**2) for i in numbers if i%2 ==0]
#     # for e in numbers:
#     #     if not e % 2:
#     #         out.append((e,e **2))
# print(out)

# ----------------------------------------------------------

# def select(f, col):
#     return[f(x) for x in col] 

# def where(f,col):
#     return[x for x in col if f(x)]
     
# data = '1 2 3 5 8 15 23 38'.split()     

# res = select(int, data)
# print(res)
# res = where(lambda x: not x%2,res)
# print(res)
# res = select(lambda x:(x, x**2),res)
# print(res)

# OR
# data = '1 2 3 5 8 15 23 38'.split()  
# res = map(int,data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x ,x ** 2),res))
# print(res)



# ______________________________________________________

                                        # MAP - map(f(x),data)
#    Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
# ↓ ↓ ↓ ↓ ↓
# [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# li = [x for x in range(1,21)]
# li = list(map(lambda x: x+10, li))
# print(li)
# _____________________________________________________________


# data = map(int,input().split())
# data = map(int,'1 2 3 4 555 6'.split()) - # ДАННЫЕ СОХРАНЕНЫ В MAP
# # data = list(map(int,'1 2 3 4 555 6'.split())) # Преобразованы в лист
# for e in data:
#     print(e)
# _________________________________________________________________
                                        # FILTER - 
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
# ↓
# [ 2, 4 ]
# Нельзя пройтись дважды

# data = [x for x in range (10)]
# res =  list(filter(lambda x: not x%2, data))
# print(res)
# _______________________________________________________________
                        #       ZIP``
                        #Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
# ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды 

# users =['user1','user2','user3','user4','user5']
# ids = [4,5,9,14,7]

# data = list(zip(users, ids))
# print(data)
# ----------------------------------------------------------------------
                            # Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users =['user1','user2','user3','user4','user5']
data = list(enumerate(users))
print(data)