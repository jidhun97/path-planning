
import csv


mycsv = csv.reader(open("Co-ordinates - Sheet1.csv"))
dct = {}
for lines in mycsv:
    dct[lines[0]] = lines[1:]
dct.pop('Point')
