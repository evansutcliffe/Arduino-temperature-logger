# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:46:04 2019

@author: evans
"""

# fakeSerial.py
# D. Thiebaut
# A very crude simulator for PySerial assuming it
# is emulating an Arduino.
#from http://pyserial.sourceforge.net/shortintro.html
import threading
import time
import random
import io
# a Serial class emulator 


class Serial:

    ## init(): the constructor.  Many of the arguments have default values
    # and can be skipped when calling the constructor.
    def __init__( self, port='COM1', baudrate = 19200, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0):
        self.name     = port
        self.port     = port
        self.timeout  = timeout
        self.parity   = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff  = xonxoff
        self.rtscts   = rtscts
        self._isOpen  = True
        self._in_waiting = 0
        self._receivedData = ""
        self._data = ""
        self.temp=25.0
        self.humidity=50
        self._thread=threading.Thread(name=('arduino '+str(self.name)), target=self.setup)
        self._thread.start()


    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen( self ):
        return self._isOpen
    
    def setup(self):
        self.loop()
        return
    
    def loop(self):
        previous_time=time.clock()
        while(self._isOpen):
            if(time.clock()-previous_time>1):
                previous_time=time.clock()
                self.temp=self.temp+random.uniform(5, 0)-2.5
                self.humidity=self.humidity+random.uniform(10, 0)-5
                data=str(self.temp)+','+str(self.humidity)+'\n'
                self._data= data#"25.0,60.0\n"
                #self._data=ascii(data)
                #self._in_waiting=len(data)
                self._in_waiting=1

    ## open()
    # opens the port
    def open( self ):
        self._isOpen = True
        #self._thread = threading.Thread(target=run_backgroud, args=(self,))
        #self._thread.start()
        #self._thread.join()

    ## close()
    # closes the port
    def close( self ):
        self._isOpen = False
        
    def inWaiting( self ):
        return self._in_waiting
    ## write()
    # writes a string of characters to the Arduino
    def write( self, string ):
        print( 'Arduino got: "' + string + '"' )
        self._receivedData += string

    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read( self, n=1 ):
        s = self._data[0:n]
        self._data = self._data[n:]
        self._in_waiting=len(self._data)
        #print( "read: now self._data = ", self._data )
        return s.encode()

    ## readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline( self ):
        returnIndex = self._data.index( "\n" )
        if returnIndex != -1:
            s = self._data[0:returnIndex+1]
            self._data = self._data[returnIndex+1:]
            self._in_waiting=0
            self._data = ''
            return s.encode()
        else:
            return ""
        
        
    def available(self):
        return len(self._data)
    ## __str__()
    # returns a string representation of the serial class
    def __str__( self ):
        return  "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % ( str(self.isOpen), self.port, self.baudrate ) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)"\
               % ( self.bytesize, self.parity, self.stopbits, self.xonxoff,
                  
                   self.rtscts )

        