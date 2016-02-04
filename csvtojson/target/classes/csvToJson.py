import json
import csv

a= """column1;column2;column3;column4;column5
abc;def;dghi;jkl;mno
pqr;stu;vwx;;"""

#get rows of the csv file
rows=a.splitlines()

#get the headers from the csv file
fieldnames=rows[0].split(';')

#Delete the rows containing headers
rows.pop(0)

#read CSV and convert csv to Json
reader = csv.DictReader(rows, fieldnames, delimiter=';')
out = json.dumps([ row for row in reader ], sort_keys=True)

result=out