def checker(data = ""):
    useful_sumbol = ("(",")","+","-","/","*",",","."," ") 
    data_temp = data
    for letter in data:
        if not letter.isdigit() and (not letter in useful_sumbol):
            data_temp = data_temp.replace(letter,"")
    return data_temp

print(checker("(0,1) aaa  - yyy (2,7)"))