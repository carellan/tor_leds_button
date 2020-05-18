from gpiozero import Button, LED
import os
from time import sleep
from datetime import datetime
from write_logs import write_line_log

button = Button(15)
magenta_led = LED(26) #Magenta
cian_led = LED(13) #Cian
yellow_led = LED(19) #Yellow

is_first = True
last_value = button.value

logs_directory = 'logs'


while True:
    status_tor = os.system('service tor status > log.log')

    if is_first:
        write_line_log(logs_directory,'Primera comprobación')
        print('Primera comprobación')
        if status_tor == 0:
            write_line_log(logs_directory, '[Primera comprobación] TOR ON - Aplicando IP_Tables')
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_tor.sh')
        else:
            write_line_log(logs_directory, '[Primera comprobación] TOR OFF - Aplicando IP_Tables')
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_ap.sh')
        is_first = False

    if button.value != 0:
        print('Boton pulsado')
        write_line_log(logs_directory, 'Botón pulsado')

        if status_tor == 0:
            magenta_led.off()
            yellow_led.on()
            os.system('service tor stop')
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_ap.sh')
            write_line_log(logs_directory, '[Botón pulsado] TOR Apagado')
            print('Tor parado')
        else:
            magenta_led.off()
            cian_led.on()
            os.system('/root/tor_leds_button/flush_iptables.sh')
            os.system('/root/tor_leds_button/iptables_tor.sh')
            os.system('service tor start')
            write_line_log(logs_directory, '[Botón pulsado] TOR Encendido')
            print('Tor encendido')
        sleep(2)



