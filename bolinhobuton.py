from serial import *
from time import *
c = 0

serialport = Serial('COM3',9600)


while True:

    if serialport.read() == b'1' :
        print('Bolinho é foda')
        c = c+1
        print(c)
        sleep(2)
        



