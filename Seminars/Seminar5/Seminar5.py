# def f(a=None):
#     if a == None:
#         a= []
#     a.append(len(a))
#     return a

# l = [0, 1, 2]

# print(f(l))
# print(f(l))
# print(f(l))
# print(f(l))
# _________________________________________
# Лямбда

# a=[(6, 9), (3, 3), (-2, 3), (6, 8), (6, 4)]
# print(max (a, key=lambda с: с[1]))
# a=['1','2','10','3','9']
# print(max (a, key=int))
# ____________________________________________
# List comprehension 
# a=[]
# for n in range(11):
#     if n % 5 != 0:
#         if n % 2 == 0:
#             a.append(n*n)
#         else: 
#             a.append(n**3)
# print(a)    

# b = [n*n if not n % 2 else n**3 for n in range(11) if n % 5 !=0] 
# print(b)
# _______________________________________________
# # MAP # FILTER  # ZIP

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
itog = list(map(lambda x: x**2,a))
filter_itog = list(filter(lambda x: x % 5 != 0, a))
print(f'MAP {itog}')
print(f'FILTER {filter_itog}')

b = 'abcdefghi'
c = (False, True, None)
for item in zip(a,b,c):
    print(f'ZIP {item}' )