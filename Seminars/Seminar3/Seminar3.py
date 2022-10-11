# # 1. Напишите программу, которая определит позицию второго вхождения строки в 
# #     списке либо сообщит, что её нет.

# # *Пример:*

# # - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# # - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# # - список: [], ищем: "123", ответ: -1

list_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list_2 = ["йцу"]
pos=0
result_index = 0
for i in range (len(list_1)):
    if pos == 2:
        print()
        break
    result_index = i
    string1 = list_1[i]
    string2 = list_2[0]
    for j in range (len(string1) - len(string2) + 1):
        if string2 in string1[j:j+len(string2)]:
            if pos == 2:
                break
        pos += 1 
                
                    
#     print(string1)
#     print( result_index)
#     # print(string2)
#             # pos +=1 
# # print(f'pos = {pos}')
# print(f'Искомая строка ( {string2} ) входит 2-ой раза в искомый список {list_1} на {result_index+1} позиции ')

# 2. Задайте список. Напишите программу, которая определит, 
#     присутствует ли в заданном списке строк некое число.

# dig_list = ["йцу", 123, "ячс", "цук", 6786786, "йцукен","ячс"]
# value1 = 6786786
# value2 = "ячс"
# count_digit = 0
# count_str = 0
# print(len(dig_list))
# for i in range(len(dig_list)):
#     print(f'list {i} = {dig_list[i]}')
#     if value1 == dig_list[i]:
#         count_digit +=1
#     if value2 == dig_list[i]:
#         count_str +=1


# print(f'В данном списке встречается искомое число {count_digit} раз, а искомая строка {count_str} раз ')
 