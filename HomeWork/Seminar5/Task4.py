
text = 'aaaaaaaaabbbbbbccccccchhhhhh'
print(f'Изначальный текст {text}')
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
print(f'RLE компрессия {result_string}')        

res = []
temp = []
letter =''
code = (result_string)    
for i, char in enumerate(code):
        if not char.isdigit():letter = char
        if char.isdigit():
            for j in range(int(char)):
                res.append(letter)
res = "".join(res)                
print(f'RLE декомпрессия {res}')