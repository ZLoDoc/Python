#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = ('\nИ редакабвтора и поэта не стабволько поразабвило то,' 
    ' что наабвшлась в портабвсигаре имабвенно «Наабвша марка», '
    'сколькабво саабвм портсиабвгар. Он бабвыл громаднабвых размеабвров, '
    'червонабвного золабвота, и набва крыабвшке егабво при открыабввании '
    'сверкнабвул сиабвним и беабвлым огабвнем бриллиабвантовый треугоабвльник.\n')
print(text)
# replace_text = text.replace('абв','')
# print(replace_text)

replace_text = 'абв'
result_text = ''
count = 0
print(replace_text)

for i in range(len(text)):
    for j in range(replace_text):
        if text[i+j] == replace_text[j]:
            count+=1
            if count == len(replace_text)+1:
                i = i + (len(replace_text))
    result_text + (text[i])                 
            # if text[i+j] == replace_text[j]:count+=1
            # if count == len(replace_text)+1:
            #     count = 0
            #     result_text + (text[i])
            #     i = i + (len(replace_text))
    


            # print(text[j])
print(text, count)
print(result_text)