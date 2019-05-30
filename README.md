# The Class Of IFSC

Create a Django REST service that can able to :
1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

You can use the data available in the below repository in your backend db. 

DATA SOURCE : https://github.com/snarayanank2/indian_banks

Host it in Heroku - you can signup for a free account in Heroku. 


Here are steps on how you can get a django app running in Heroku in a few minutes. 

Heroku : https://devcenter.heroku.com/articles/getting-started-with-python


Please use PostgreSQL as your backend DB. You may not be able to load the entire dataset in the free tier - you can make do with 10000 rows. Hosting in Heroku and using PostgreSQL are important parts of the coding test - the objective is to see if you can learn a new platform and be productive quickly.


# Introduction

Djangi REST service for gets details of banks in India. 


## Requirements
    pip install -r requirement.txt

## Database
    PostgreSQL

## Running the application
    Clone the project to your machine [https://github.com/Varnan/class_of_ifsc.git]
    Navigate into the diretory [cd class_of_ifsc]
    Create a virtualenv
    Install the dependencies on virtaulenv [pip install -r requirement.txt]
    Navigate into the class_of_ifsc directory [cd class_of_ifsc]
    Start the backend server [python manage.py runserver]
    Dump the sql db from the above DATA SOURCE
    Visit the application on the browser - http:localhost:8000 or Use the postman collection

## Built With
    Python - A programming language that lets you work quickly and integrate systems more effectively.
    Django - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Postman Collection
    https://www.getpostman.com/collections/73146afabb6e0545df3f