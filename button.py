from gpiozero import Button
import os
from time import sleep

button = Button(15)
is_first = True

while True:
    status_tor = os.system('service tor status > log.log')
    last_value = button.value
 
    if is_first:
        print('Primera comprobación')
        if status_tor == 0:
            os.system('./flush_iptables.sh')
            os.system('./iptables_tor.sh')
        else:
            os.system('./flush_iptables.sh')
            os.system('./iptables_ap.sh')
        is_first = False

    if button.value != 0:
        print('Boton pulsado')
        if status_tor == 0:
            os.system('service tor stop')
            os.system('./flush_iptables.sh')
            os.system('./iptables_ap.sh')
            print('Tor parado')
        else:
            os.system('./flush_iptables.sh')
            os.system('./iptables_tor.sh')
            os.system('service tor start')
            print('Tor encendido')
        sleep(3)



