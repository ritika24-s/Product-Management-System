# Product Management System

This README provides a comprehensive guide to the setup, configuration, and usage of the **Product Management System** project. This application is designed to facilitate product management for suppliers and buyers, with features that allow users to add, edit, and delete products. It also includes user authentication for better security and access control.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Database Configuration](#database-configuration)
- [Project Structure](#project-structure)
- [CRUD Operations](#crud-operations)
- [Testing](#testing)
- [Running the Application](#running-the-application)
- [Using Docker](#using-docker)
- [Assignment Requirements](#assignment-requirements)

## Prerequisites

Before starting the setup, ensure that you have the following installed:

- **Python 3.11 or higher**
    ```bash
    python --version
    ```
    If Python is not installed, use the following command to install:
    ```bash
    sudo apt update && sudo apt install python3 python3-virtualenv
    ```

- **PostgreSQL 3.11 or higher**
    ```bash
    psql --version
    ```
    If PostgreSQL is not installed, use the following command to install:
    ```bash
    sudo apt install postgresql postgresql-contrib
    ```

## Setup Instructions

1. **Set up PostgreSQL Database**  
   Follow the instructions in the `db` file to set up your PostgreSQL database.

2. **Install Virtual Environment**  
   Install the virtual environment package:
   ```bash
   pip install virtualenv
   ```

3. **Create a Virtual Environment**  
   Create a virtual environment for the project:
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**  
   Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Libraries**  
   Install the necessary Python libraries:
   ```bash
   pip install Django psycopg2-binary pillow python-decouple
   ```

6. **Create Django Project**  
   Create a new Django project:
   ```bash
   django-admin startproject product_management
   cd product_management
   ```

7. **Connect the Database**  
   Update the `settings.py` file to configure the default database settings.

8. **Create Django Apps**  
   Create two Django apps for this project:
   ```bash
   python manage.py startapp products
   python manage.py startapp users
   ```
   Add both apps to the `INSTALLED_APPS` section in `settings.py`.

9. **Create Models**  
   Define the models for products and users:
   - Set `AUTH_USER_MODEL = 'users.User'` in `settings.py`.

10. **Run Migrations**  
    Apply the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    After each migration, permissions will be created as defined in `signals.py`. You can also run:
    ```bash
    python manage.py create_groups
    ```

11. **Add a Superuser**  
    Create a superuser to test the functionality:
    ```bash
    python manage.py createsuperuser
    ```

## Project Structure

The project structure is organized to enhance clarity and maintainability. Here is a brief overview of the folder structure:

```
product_management/
 ┣ products/                   # App for product management
 ┃ ┣ migrations/               # Database migrations
 ┃ ┣ tests/                    # Test cases
 ┃ ┣ admin.py                  # Admin interface configuration
 ┃ ┣ forms.py                  # Product forms
 ┃ ┣ models.py                 # Product models
 ┃ ┣ urls.py                   # URL configurations for products
 ┃ ┣ views.py                  # View functions for products
 ┣ users/                      # App for user management
 ┃ ┣ migrations/               # Database migrations
 ┃ ┣ tests/                    # Test cases
 ┃ ┣ admin.py                  # Admin interface configuration
 ┃ ┣ forms.py                  # User forms
 ┃ ┣ models.py                 # User models
 ┃ ┣ urls.py                   # URL configurations for users
 ┃ ┣ views.py                  # View functions for users
 ┣ templates/                  # HTML templates
 ┃ ┣ buyer/                    # Templates for buyers
 ┃ ┣ supplier/                 # Templates for suppliers
 ┣ .env                        # Environment variables
 ┣ manage.py                   # Django management script
 ┣ product_management/         # Project settings
 ┃ ┣ settings.py               # Project settings
 ┃ ┣ urls.py                   # Project URLs
 ┃ ┣ wsgi.py                   # WSGI application
```

## CRUD Operations

The application provides Create, Read, Update, and Delete (CRUD) operations for product management:

- **Create**: Suppliers can add new products using the `add_product.html` form.
- **Read**: Both buyers and suppliers can view products on the product listing page.
- **Update**: Suppliers can edit existing products using the `edit_product.html` form.
- **Delete**: Suppliers can delete products using the `delete_product.html` confirmation page.

There are additional features as well:
- **Cheaper Analogues**: Suppliers can see list of products which are provided at a cheaper price by other suppliers. Note - The product code should be same for the products to appear in the list.

## API Endpoints

The application includes several key API endpoints to facilitate interaction between the frontend and backend. Here are some of the important endpoints:

### User Authentication

POST /account/signup/: Sign up page to create buyers and suppliers. **Note** - Only Admins can access this page.
POST /account/login/: Log in as either buyer, supplier or admin.
    On successful login, different users will be redirected to different pages.
POST /account/logout/: Log out the user, invalidating their authentication token.

### Product Management

GET /products/: List of all products. The view differs for different types of users
POST /api/products/: Add a new product (suppliers only).
PUT /api/products/<id>/: Update a product (suppliers only).
DELETE /api/products/<id>/: Delete a product (suppliers only).
GET /api/products/cheaper_analogues/: Retrieve cheaper analogue products for comparison. (suppliers only).

These endpoints are designed to enable seamless communication between the frontend and backend, ensuring a smooth user experience.

## Testing

The project follows a Test-Driven Development (TDD) approach. Test cases are created in the `tests` directory within each app. To run the tests, use the following command:

```bash
python manage.py test
```

## Running the Application

To start the Django development server, use:

```bash
python manage.py runserver
```

Access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Using Docker

If you prefer to use a Docker image for deployment, you can pull my pre-built Docker image:

```bash
docker pull ritikasharma24/django-app
```

## Assignment Requirements

This project has been developed in alignment with the assignment requirements present in the folder Project Requirements.md
Please feel free to reach out in case of any questions - sharmari@tcd.ie
