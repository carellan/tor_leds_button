from gpiozero import Button
import os
from time import sleep

button = Button(27)
while True:
    last_value = button.value
    if button.value != last_value:
        os.system('reboot')
        last_value = button.value

