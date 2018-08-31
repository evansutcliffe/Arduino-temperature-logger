import serial
import csv
import collections
import numpy as np
from datetime import datetime
import sys 

arduino = serial.Serial('\.\COM3', 9600,timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
if not arduino.is_open:
    arduino.open()
    if (arduino.is_open):
        print("okay")
    else :
        print("not connected")
        exit()
#THT=np.array([],[],[])
T=[]
H=[]
t=[]
count =0  

while(arduino.is_open):
    try :
        b_data =arduino.readline()
        temp = b_data.decode().split() #split string into a list  
        if (len(temp)):
            if (temp[0]=='Temperature'):
                T.append(temp[2])
                t.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                H.append(temp[2])
    except  :    
        arduino.close() # if an error is thrown... such as the serial dieing
# serial has closed

with open('data.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
    w.writerow(["datetime","temp/degrees C","humidity/RH"])
    for line in (zip(t,T,H)):
        w.writerow(line)

        
        


