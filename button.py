from gpiozero import Button
import os
from time import sleep

button = Button(15)
counter = 0
while True:
    last_value = button.value
    status_tor = os.system('service tor status')
    if button.value != last_value:
        if status_tor == 0:
            os.system('service tor stop')
            os.system('./flush_iptables.sh')
            os.system('./iptables_ap.sh')
            print('stop')
        else:
            os.system('./flush_iptables.sh')
            os.system('./iptables_tor.sh')
            os.system('service tor start')
            print('on')
        last_value = button.value

