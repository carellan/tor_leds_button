apt install virtualenv
virtualenv venv -p python3
venv/bin/pip install -r requirements.txt
./install_services.sh
