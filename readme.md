**Setup**

`git clone https://github.com/Benjamin-LucasM/Message-app.git`
`cd Message-app/`
`python3 -m venv .venv`
*sudo apt install python3* if python is not previously installed
`source .venv/bin/activate`
`cd messageapp/`
`pip install -r requirements`

**Run server**

`source .venv/bin/activate`
`python3 manage.py runserver`

**Shut down**

sudo lsof -i :8080

