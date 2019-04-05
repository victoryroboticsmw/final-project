from gpiozero import LED, Button
from time import sleep

green = LED(4)
button = Button(2)
blue = LED(17)

while True:
    button.when_pressed = green.on  
    blue.on()
    green.on()
    sleep(1)
    button.when_released = green.off
    blue.off()
    green.off()
    sleep(1)
button.when_pressed = blue.off
button.when_released = blue.on
