
from datetime import datetime
import time


import plot_data
#import email_me 


serial_port='\.\COM5'
real_serial=0
temperture=[]
humidity=[]
T=[]
cold_list=[]






def process_data(data,is_cold,n):
    COLD_LIMIT=10
    if (len(data) > 0):
        temperture.append(float(data[0]))
        humidity.append(float(data[1]))    
        T.append(n)
        if (float(data[0])<COLD_LIMIT):
           is_cold=1 
           cold_list.append((float(data[0]),float(data[1]),datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) # record start of cold time period
        else:
            is_cold=0
    return is_cold


def run_serial(ser):
    if not ser.isOpen():
        ser.open()
        time.sleep(1)
    if not (ser.isOpen()):
        print("can't connect")
        exit()
        print("okay")  
    run=1
    count = 0
    is_cold=0
    start_time = time.time()  
    try:
        while (run):      
            try :
                while(ser.inWaiting() > 0 ): 
                    b_data =ser.readline().strip()
                    temp = b_data.decode().split(',')#.decode().split() #split string into a list  
                    n=float (time.time() - start_time)
                    is_cold=process_data(temp,is_cold,n)
                    print(temp)
                    if(is_cold):
                        print("WARNING V COLD")
                        print(temp)
                    #plot_data()
            except KeyboardInterrupt as e:
                run = 0          
                print(e)
            except Exception as e :   
                print(e)
                count=count+1
                if (count>3):
                    run=0
    except:
        pass
    ser.close()  
    # serial has closed


if(real_serial):
    import serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)    
else:
    import FakeArduino as serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0)
    
run_serial(arduino) 
title=["datetime","temp/degrees C","humidity/RH"]
plot_data.plot_data(T, temperture,humidity)

print("finished")
