import csv
with open('projectnurse.csv', newline='\n') as csvfile:
    nurseinfo = csv.reader(csvfile, delimiter=',')
    for row in nurseinfo:
        print(',\n '.join(row))
