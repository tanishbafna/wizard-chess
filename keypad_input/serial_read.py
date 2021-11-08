import os
import serial

COM_PORT = '/dev/tty.X5-SerialPort'
file_name = 'input_moves.txt'
FILE = os.getcwd() + '/' + file_name
ser = serial.Serial(COM_PORT, 9600)

while True:
    with open(FILE, 'w') as f:
        existing = f.read().strip()
        if len(existing) == 2: 
            f.write(existing + ser.readline().decode("utf-8").strip())
        else:
            f.write(ser.readline().decode("utf-8").strip())

ser.close()