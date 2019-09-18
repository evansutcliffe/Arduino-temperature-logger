# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:11:40 2019

@author: evans
"""
import matplotlib as mpl
import matplotlib.pyplot as plt


def write_data(title,time,temperture,Humidity):
    with open('data.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        w.writerow(title)
        for line in (zip(time,temperture,humidity)):
            w.writerow(line)
 
def plot_data(T,temperture,humidity):#x,y,time_data):

    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot(1,1,1)


    ax1.plot(T, temperture)
    ax1.plot(T, humidity)
