# n = int(input())
# num = 1
# for i in range(n):
#     print(num)
#     num *= -3
# n = int(input())
# for i in range (n):
#     print(3*(i+1)+1)
string1 = input('Введите первую строку: ')
string2 = input('Введите вторую строку: ')
result = 0
if len(string1)>len(string2):
    for i in range (len(string1) - len(string2) + 1):
        if string2 in string1[i:i+len(string2)]:
            result += 1
            s=0
else:
    for i in range (len(string2) - len(string1) + 1):
        if string1 in string2[i:i+len(string1)]:
            result += 1
            s=1
if s == 0:
    print(f'Строка "{string2}" встречается в строке "{string1}" {result} раз')
elif s==1:
    print(f'Строка "{string1}" встречается в строке "{string2}" {result} раз')    
