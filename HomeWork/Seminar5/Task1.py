#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = ('\nИ редакабвтора и поэта не стабволько поразабвило то,\n')
print(text)
# replace_text = text.replace('абв','')
# print(replace_text)

replace_text = 'абв'
result_text = ''
count = 0
print(replace_text)


for i in range(len(text)-len(replace_text)):
    for j in range(len(replace_text)):
        # print(f'i={i}')
        # print(f'   j={j}')
        # print(f'      i+j={i+j}')
        if text[(i+j)] == replace_text[j]:
           count+=1
        else: count = 0
        if count == len(replace_text):
            i = i + (len(replace_text))
    result_text = result_text +  (text[i])                 
            # if text[i+j] == replace_text[j]:count+=1
            # if count == len(replace_text)+1:
            #     count = 0
            #     result_text + (text[i])
            #     i = i + (len(replace_text))
    


            # print(text[j])
# print(text, count)
print(result_text)

# // Дан текст. В тексте нужно все пробелы 
# // заменить черточками, 
# // маленькие буквы "к" заменить большими "К", 
# // а большие "С" на маленькие "с"

# string text = "— Я думаю, — сказал князь, улыбаясь, — что,"
# + "ежели бы вас послали вместо нашего милого "
# + "Винценгероде, вы бы взяли приступом согласие"
# + "прусского короля. Вы так красноречивы. Вы "
# + "дадите мне чаю?";

# //string s = "qwerty"
# //            012 
# // s[3] = r

# string Replace(string text, char oldValue, char newValue)
# {
#     string result = String.Empty;
#     int length = text.Length;
#     for (int i = 0; i < length; i++)
#     {
#         if (text[i] == oldValue) result = result + $"{newValue}";
#         else result = result + $"{text[i]}";

#     }
#     return result;
# }
# string newText = Replace(text, ' ', '|');
# Console.WriteLine(newText);
# Console.WriteLine("");
# newText = Replace(newText, 'к', 'К');
# Console.WriteLine(newText);
# Console.WriteLine("");
# newText = Replace(newText, 'с', 'С');
# Console.WriteLine(newText);