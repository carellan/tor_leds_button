# tor_leds_button

## Howto
~~~
$ git clone https://github.com/carellan/tor_leds_button.git
$ cd tor_leds_button
$ apt-get install -y virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
$ chmod +x install_services.sh
$ ./install_services.sh


////THIS JUST IF WE WANT TO EXECUTE THEM MANUALLY, installer already starts thems
(venv)$ pyhton example.py
(venv)$ python boton.py
~~~ 




## TODOs

- [x] Services to start pyhton scripts.
