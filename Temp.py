
res = []
# result
temp = []
leter =''
code = ('a5b6c7h6')
# res.append(code.split())
# print(res)
for i, char in enumerate(code):
        temp.append(char)       
for i, char in enumerate(temp):
        if not char.isdigit():leter = char
        if char.isdigit():
            for j in range(int(char)):
                res.append(leter)
print(res)
    




# for j in range(len(res)):
#     print(res[j])
#     if res[j].isdigit(): 
#         for n in range(int(res[j])):itog + str((res[j-1]))
#     else: continue
