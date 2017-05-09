import csv
import pandas as pd
import numpy as np

# with open('projectnurse.csv', newline='\n') as csvfile:
    # nurseinfo = csv.reader(csvfile, delimiter=',')
    # for row in nurseinfo:
    #     print(',\n '.join(row))


df = pd.read_csv('projectnurse.csv')
print(df)
