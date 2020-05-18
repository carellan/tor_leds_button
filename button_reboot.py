from gpiozero import Button
import os
from time import sleep
from write_logs import write_line_log

logs_directory = 'logs'

button = Button(27)
while True:
    last_value = button.value
    if button.value != last_value:
        write_line_log(logs_directory, 'Reboot button pulsado')
        os.system('reboot')
        last_value = button.value

