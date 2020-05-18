from gpiozero import LED
from time import sleep
import os
from write_logs import write_line_log

cian_led = LED(13) #Cian
yellow_led = LED(19) #Yellow
magenta_led = LED(26) #Magenta

def off_all_leds(cian, yellow, magenta):
    cian.off()
    yellow.off()
    magenta.off()

logs_directory = 'logs'

write_line_log(logs_directory, 'leds iniciado')

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
    sleep(1)
