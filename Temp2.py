import csv
def csv_export():
    with open('file.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
csv_export()