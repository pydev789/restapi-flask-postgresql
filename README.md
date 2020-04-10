# restapi-flask-postgresql
A RESTful API created using Flask and SQLAlchemy that interacts with a PostgreSQL database of users.
Python Version Used: Python 3.6.0

### Installation:

1) Setup a virtual environment in the project folder using python3: `$ python -m venv /path/.../venv`
2) Start the virtual environment. You should see `(venv)` in as part of the command prompt once it is started: `$ source /path/.../venv/Scripts/activate`
*NOTE*: To stop the virtual environment at any time, run `(venv) $ deactivate`
3) Install all the requirements, including flask. Be sure not to use `sudo` as this will install flask in the global environment instead of the virtual environment: `(venv) $ pip3 install -r requirements.txt`
4) Start PostgreSQL run `$ psql -U s"erver name"`. Then, create a database called user_reviews by running `# CREATE DATABASE users;`
5) Finally, run `# \q` to quit psql, and back in the original terminal window run `(venv) $ python setup.py` to initialize the database tables.

### To Run:

1) Set an export path for flask: `(venv) $ export FLASK_APP=app.py`
2) Run flask! `(venv) $ flask run`
3) Go to http://127.0.0.1:5000 in a browser


# API Documentation

GET /monsters/:id

GET /monsters

POST /monsters

PUT /monsters/:id

DELETE /monsters/:id