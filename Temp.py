from audioop import mul




my_string = str.replace(my_string, "- ", "+ -").split()
my_string = list(filter(lambda x: x != "+" and x != "=" and x != "0", my_string))
    for i in range(len(my_string)):
        my_string[i] = my_string[i].split("*")