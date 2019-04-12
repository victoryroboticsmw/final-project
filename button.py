from gpiozero import LED, Button
from time import sleep

flappyboi = LED(25)
green = LED(4)
button = Button(2)
red = LED(17)

while True:
    green.on
    sleep(1)
    Green.off
    sleep(1)
    red.on()
    sleep(1)
    red.off()
    sleep(1)
