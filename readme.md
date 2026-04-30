**About**


This is a messaging app that allows you to privatly message users in your local network. 


**features**


user regristration

search for spesific users

encrypted messages

delete messages


**requirements**

- python 3.1+

- pip

- screen (`sudo apt install screen`)


**Setup**



`git clone https://github.com/Benjamin-LucasM/Message-app.git`

`cd Message-app/`

`python3 -m venv .venv`

*sudo apt install python3* if python is not previously installed

`source .venv/bin/activate`

`pip install -r requirements.txt`

`cd messageapp`

`python3 manage.py migrate`

`python3 manage.py createsuperuser` this will be the admin user


**Run server**


`screen -S messageapp`

`source .venv/bin/activate`

`cd messageapp`

`python3 manage.py runserver <ip-adress>:port`

press ctrl + a 

press d

`exit`


**Shut down**


`screen -r messageapp`

press ctrl + c

press ctrl + a

press d

`screen -ls`

`screen -X -S <id> quit`