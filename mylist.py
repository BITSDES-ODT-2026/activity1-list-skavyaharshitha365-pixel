from machine import Pin,PWM
import time

l1,l2,l3,l4= Pin(5,Pin.OUT),Pin(4,Pin.OUT),Pin(13,Pin.OUT),Pin(1,Pin.OUT)
l=[l1,l2,l3,l4]

while True:
    for i in l:
        i.value(1)
        time.sleep(0.4)
        i.value(0)
        time.sleep(0.05)

#Create any list
