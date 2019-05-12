#### Created by: Abdulaziz Al-Sakhbouri
#### Date: 7 May 2019
#### For Support: supermind92@gmail.com 
#### #######################################
#### This python library to program UHF Reader WRD-130-U1
####
#### Serial port: /dev/ttyACM0
#### baudrate   : 115200
####
#### Note: You must install pySerial python library by write the following command in Terminal:
#### pip install pyserial
####
#### or go to github: https://github.com/pyserial/pyserial

import serial

ser = serial.Serial("/dev/ttyACM0",115200)

def readRFID(n , D):
    ser.write(D.encode('utf-8'))
    B = ser.inWaiting()
    while(B==0):
        B = ser.inWaiting()
    data = ser.read(B).decode('utf-8').rstrip()
    i = 0
    d = ""
    for c in data:
        if (i>n):
            d += c
        i += 1
    return d

def writeCMD(D):
    ser.write(D.encode('utf-8'))
    B = ser.inWaiting()
    while(B==0):
        B = ser.inWaiting()
    data = ser.read(B).decode('utf-8').rstrip()
    i = 0
    d = ""
    for c in data:
        if (i>0):
            d += c
        i += 1
    return d

def getID():
    D = "Q\r"
    return readRFID(1 , D)

def getMultiID():
    D = "U\r"
    return readRFID(1 , D)

def getMem(a,b,c):
    D = "R" + str(a) + "," + str(b) + "," + str(c) +"\r"
    return readRFID(1 , D)

def putMem(a,b,c,d):
    D = "W" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "\r"
    return readRFID(0 , D)