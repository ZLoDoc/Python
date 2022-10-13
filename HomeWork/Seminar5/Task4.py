# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
text = 'jjjjjddddddddrrrrrrrraaaac'
n = 0
nachalo = n
count = 0
lenght = len(text)
# for i in range(lenght):
while lenght != 0 and text[n] == text[nachalo]:
    count = count+1
    n = n + 1
    lenght = lenght-1 
    
else:
    result_string = text[nachalo] + str(count)
    nachalo = n
    count = 0
lenght = lenght-1