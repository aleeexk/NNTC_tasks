import re
import csv

tsv = open('output_test.tsv', 'r')
fileContent = tsv.read()

fileContent = re.sub("\t", ",", fileContent)
csv_file = open("csv.csv", "w")
csv_file.write(fileContent)
csv_file.close()

with open('csv.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    alot = list(reader)
    initial = alot[5]
    ended = alot[58]

dict1 = dict(zip(headers, initial))
dict2 = dict(zip(headers, ended))
print(dict1.keys())
print(dict1.values())

with open('bc_dicts.txt', 'w') as out:
    out.write('Begin')
    for key, val in dict1.items():
        out.write('{}:{}\n'.format(key, val))
    out.write('\nEnd')
    for key, val in dict2.items():
        out.write('{}:{}\n'.format(key, val))
