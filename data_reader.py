# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:53:46 2018

@author: evans
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

t=[]
T=[]
H=[]
with open('data.csv', "rt") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            t=", ".join(row)
            print (t)
            line_count += 1
        else:
            #t.append([row[0]])
            T.append(row[1])
            H.append(row[2])
            #print(f'\t{row[0]} {row[1]} {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
fig=plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(T)
ax1.set_ylabel('T')

ax2 = ax1.twinx()
ax2.plot(H, 'r-')
ax2.set_ylabel('H', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
fig2=plt.figure()
plt.scatter(H,T)