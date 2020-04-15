from gpiozero import LED
from time import sleep
import os

cian_led = LED(21) #Cian 
yellow_led = LED(20) #Yellow
magenta_led = LED(16) #Magenta

def off_all_leds(cian, yellow, magenta):
    cian.off()
    yellow.off()
    magenta.off()

while True:
    status_tor = os.system('service tor status')
    if status_tor == 0: #Tor on
        off_all_leds(cian_led, yellow_led, magenta_led)
        magenta_led.on()
        cian_led.on()
    else:
        off_all_leds(cian_led, yellow_led, magenta_led)
        magenta_led.on()
        yellow_led.on()
    sleep(2)
