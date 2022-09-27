#   3. Напишите программу, в которой пользователь будет задавать две строки,
#      а программа - определять количество вхождений одной строки в другой.
#      ssabababsdaasd aba -> 2
string1 = input('Введите первую строку: ')
string2 = input('Введите вторую строку: ')



def f(a,b):
    result = 0
    for i in range (len(string1) - len(string2) + 1):
        if string2 == string1[i : i + len(string2)]:
            result += 1
    return(result)

print(f'Строка "{string2}" встречается в строке "{string1}" {f(string1,string2)} раз')

