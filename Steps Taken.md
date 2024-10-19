<!-- This file is to demonstrate the steps I took for creating this project
Please follow along if you wish to replicate
Or if you wish to understand on what was done
Thank you!!
 -->
Check Python version (should be greater than 3.11)
    python --version == 3.12.4
    Install if not present - sudo apt update && sudo apt install python3 python3-virtualenv
Check PostgreSQL version (should be greater than 3.11)
    psql --version == psql (PostgreSQL) 17.0
    Install if not present - sudo apt install postgresql postgresql-contrib

Set up PostgreSQL Database
    Instructions in db file

Install Virtual Environment
    pip install virtualenv
Create Virtual Environment 
    python -m venv venv
Activate the virtual environment
    venv\Scripts\Activate.ps1 (I am on windows)

Install libraries
    pip install Django psycopg2-binary pillow python-decouple

Create Django project
    django-admin startproject product_management
    cd product_management

Connect the Database to the project by adding Default Database in settings.py

Create two django apps for this project - products (for product) and users (to deal with User management)
    python manage.py startapp products
    python manage.py startapp users
    Add both the apps to INSTALLED_APPS in settings.py

Create Models for products and users
    Set AUTH_USER_MODEL = 'users.User' in settings.py
    run migrations - 
    1. python manage.py makemigrations
    2. python manage.py migrate
    After each migrate, permissions will be created as they are stored in signals.py
    But they can be manually run - python manage.py create_groups

Add a superuser to be able to test the code functionalities - python manage.py createsuperuser

Add CRUD operations and respective HTML forms, views and URLS according to the requirement

I have kept the templates folder outside of both the apps, due to the intertwining nature of the pages.
For this reason, I have updates the Dir in Templates list inside settings.py

Create tests to follow a TDD structure. I have created tests/ folder containing test_modules.py inside each app to thoroughly test the codebase and required functionalities



Command to run the test - python manage.py test

Command to run the server - python manage.py runserver



To use my docker image instead - docker pull ritikasharma24/django-app
