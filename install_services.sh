cp ./leds.service /etc/systemd/system
cp ./button.service /etc/systemd/system

systemctl daemon-reload

service leds start
systemctl enable leds

service button start
systemctl enable button
