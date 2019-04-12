from gpiozero import LED, Button
from time import sleep

flappyboi = LED(25)
green = LED(4)
button = Button(2)
blue = LED(17)

while True:
    button.when_pressed = green.on  
    button.when_released = green.off
button.when_pressed = blue.off
button.when_released = blue.on
button.when_released = flappyboi.on
button.when_pressed = flappyboi.off
