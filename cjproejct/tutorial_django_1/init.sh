python -m pip3 install virtualenv || echo 'alreday virtualenv exists'
virtualenv fcdjango_env

source $(pwd)/fcdjango_env/bin/activate
pip install django

django-admin startproject fc_community

docker build -t cjdockerimage:v1 ./
doerk run --name cjdjango -p 8000:8000 cjdockerimage:v1 