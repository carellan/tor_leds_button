from gpiozero import Button
import os
from time import sleep

button = Button(15)
is_first = True
last_value = button.value

while True:
    status_tor = os.system('service tor status > log.log')
    
    if is_first:
        print('Primera comprobación')
        if status_tor == 0:
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_tor.sh')
        else:
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_ap.sh')
        is_first = False

    if button.value != 0:
        print('Boton pulsado')
        if status_tor == 0:
            os.system('service tor stop')
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_ap.sh')
            print('Tor parado')
        else:
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_tor.sh')
            os.system('service tor start')
            print('Tor encendido')
        sleep(4)



