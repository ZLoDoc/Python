# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
text = 'aaaaabbbbbbccccccchhhhhh'
pos = 0
nachalo = pos
count = 0
result_string = ''
for i in range(len(text)):
    if text[pos] == text[nachalo]:
        count = count+1
        pos = pos + 1
    elif text[pos] != text[nachalo]:
        result_string = result_string + text[nachalo] + str(count)
        nachalo = i
        pos = pos + 1
        count = 1
result_string = result_string + text[nachalo] + str(count)        
print(result_string)        