**Setup**

`git clone https://github.com/Benjamin-LucasM/Message-app.git`
`cd Message-app/`
`python3 -m venv .venv`
*sudo apt install python3* if python is not previously installed
`source .venv/bin/activate`
`cd messageapp/`
`pip install -r requirements`

**Run server**

`screen -S messageapp`
`cd ..`
`source .venv/bin/activate`
`cd messageapp/`
`python3 manage.py runserver <ip-adress>:port`
press ctrl + a 
press d
`exit`

**Shut down**

`screen -r messageapp`
press ctrl + c
press ctrl + a
press d