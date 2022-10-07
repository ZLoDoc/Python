# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.write('colors\n') # разделителей не будет
# data.close()
with open('file.txt', 'a') as data:
    data.write('line pppppp 1')
    data.write('line 2\n')
