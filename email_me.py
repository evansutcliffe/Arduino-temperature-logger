import serial
import csv
from datetime import datetime
##
serial_port='\.\COM3'


##
arduino = serial.Serial(serial_port, 9600,timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
if not arduino.is_open:
    arduino.open()
    if (arduino.is_open):
        print("okay")
    else :
        print("not connected")
        exit()
temperture=[]
humidity=[]
time=[]
count =0  
cold_list=[]
is_cold=0
while(arduino.is_open):
    try :
        b_data =arduino.readline()
        temp = b_data.decode().split() #split string into a list  
        if (len(temp)):
            if (temp[0]=='Temperature'):
                temperture.append(temp[2])
                time.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                humidity.append(temp[2])
            if (temp[2]<16.0 and not is_cold):
               is_cold=1 
               cold_list.append(time[-1]) # record start of cold time period
            else (temp>16.0 and is_cold):
               is_cold=0
               cold_list.append(time[-1]) # record end of cold period
            
    except :    
        arduino.close() # if an error is thrown... such as the serial dieing
# serial has closed

def write_data(time,temperture,Humidity):
    with open('data.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        w.writerow(["datetime","temp/degrees C","humidity/RH"])
        for line in (zip(time,temperture,Humidity)):
            w.writerow(line)
