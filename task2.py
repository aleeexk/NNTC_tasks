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

with open('bc_dicts.txt', 'w') as out:
    out.write('Begin')
    for key, val in dict1.items():
        out.write('{}:{}\n'.format(key, val))
    out.write('\nEnd')
    for key, val in dict2.items():
        out.write('{}:{}\n'.format(key, val))

i = 7
bigdict = []
while i < 57:
    dictn = dict(zip(headers, alot[i]))
    bigdict.append(dictn)
    i = i + 1

n = 0
while n < 50:
    x = (bigdict[n].get('pressure'))
    x = float(x) / 100000
    bigdict[n]['pressure'] = x
    y = (bigdict[n].get('temperature'))
    y = float(y) - 273
    bigdict[n]['temperature'] = y
    n = n + 1

with open('new.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    headers.pop(0)
    tsv_writer.writerow(headers)
    m = 0
    while m < 50:
        tsv_writer.writerow(bigdict[m].values())
        m = m + 1
