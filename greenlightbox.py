from gpiozero import LED
from time import sleep

green = LED(4)
blue = LED(17)

while True:
    blue.on()
    green.on()
    sleep(1)
    blue.off()
    green.off()
    sleep(1)
