from machine import Pin,PWM
import time

l1,l2,l3,l4= Pin(5,Pin.OUT),Pin(4,Pin.OUT),Pin(13,Pin.OUT),Pin(1,Pin.OUT)
l=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


while True:
    for i in l:
        l1.value(i[0])
        l2.value(i[1])
        l3.value(i[2])
        l4.value(i[3])
        time.sleep(0.2)
        
