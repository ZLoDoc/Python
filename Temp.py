# https://pythonworld.ru/moduli/modul-csv.html
import csv
with open('pb.csv', newline='') as data: #'чтение'
    reader = csv.reader(data)
    for row in reader:
        print(row)

import csv
with open('pb.csv', 'w', newline='') as data:#'запись'
    writer = csv.writer(data)
    writer.writerows('someiterable')        
              
