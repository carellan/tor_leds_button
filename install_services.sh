cp ./*.service /etc/systemd/system 

systemctl daemon-reload

service leds start
systemctl enable leds

service button start
systemctl enable button

service button_reboot start
systemctl enable button_reboot
