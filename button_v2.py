from gpiozero import Button
import os
from time import sleep

def flush_ip_tables():
    os.system('iptables -F')
    os.system('iptables -X')
    os.system('iptables -t nat -F')
    os.system('iptables -t nat -X')
    os.system('iptables -t mangle -F')
    os.system('iptables -t mangle -X')
    os.system('iptables -P INPUT ACCEPT')
    os.system('iptables -P FORWARD ACCEPT')
    os.system('iptables -P OUTPUT ACCEPT')


def set_tor_ip_tables():
    os.system('iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 22 -j REDIRECT --to-ports 22')
    os.system('iptables -t nat -A PREROUTING -i wlan0 -p udp --dport 53 -j REDIRECT --to-ports 53')
    os.system('iptables -t nat -A PREROUTING -i wlan0 -p tcp --syn -j REDIRECT --to-ports 9040')
    

def set_ap_ip_tables():
    os.system('sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"')
    os.system('iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE')

button = Button(15)
is_first = True


while True:
    status_tor = os.system('service tor status > log.log')
    last_value = button.value
 
    if is_first:
        print('chivato 1')
        if status_tor == 0:
            flush_ip_tables()
            set_tor_ip_tables()
        else:
            flush_ip_tables()
            set_ap_ip_tables()
        is_first = False

    if button.value != 0:
        print('chivato 2')
        if status_tor == 0:
            os.system('service tor stop')
            flush_ip_tables()
            set_ap_ip_tables()
            print('chivato stop')
        else:
            flush_ip_tables()
            set_tor_ip_tables()
            os.system('service tor start')
            print('chivato on')
        sleep(3)



