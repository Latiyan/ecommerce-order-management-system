# ecommerce-order-management-system

Below documentation takes you over a step-by-step guide to setup ecommerce order management microservice on your machine.

Requirements

Python latest version will work fine for this setup. You also need the Django and Django rest framework for this project.

Setup

The first thing to do is to clone the repository:

$ git clone https://github.com/Latiyan/ecommerce-order-management-system.git

$ cd ecommerce-order-management-system

Use python to create a new environment and activate it
$ python3 -m venv env

Once the environment is setup activate it

$ source env/bin/activate

Then install python dependencies (use the package manager pip):
(env)$ pip install -r requirements.txt

Run migrations & server:

(env)$ python manage.py migrate

(env)$ python manage.py runserver

Now the server is up and running on http://127.0.0.1:8000/.

# Headers Authentication for POST and PUT APIs
Authorization: Token pSaowjfdf2WPOkjr3o445ml098klmcpojfqPdoq3pweGF
