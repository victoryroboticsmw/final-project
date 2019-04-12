from gpiozero import LED, Button
from time import sleep

flappyboi = LED(25)
green = LED(4)
button = Button(2)
red = LED(17)

while True:
    button.when_pressed = green.on  
    button.when_released = green.off
    button.when_pressed = red.off
    button.when_released = red
    on
    red.on()
    sleep(1)
    red.off()
    sleep(1)
