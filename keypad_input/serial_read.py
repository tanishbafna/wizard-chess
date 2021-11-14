import os
import serial

COM_PORT = '/dev/cu.usbserial-1410'
file_name = 'input_moves.txt'
FILE = os.getcwd() + '/' + file_name
ser = serial.Serial(COM_PORT, 9600)

while True:
    with open(FILE, 'r+') as f:
        existing = f.read().strip()
        if len(existing) == 2: 
            f.write(existing + ser.readline().decode("utf-8").strip())
        else:
            f.truncate(0)
            f.write(ser.readline().decode("utf-8").strip())

ser.close()