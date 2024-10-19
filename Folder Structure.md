product_management
 ┣ products - handles the products app, which likely manages the product-related features like adding, editing, viewing, and deleting products.
 ┃ ┣ migrations
 ┃ ┣ tests
 ┃ ┃ ┣ manage.py
 ┃ ┃ ┣ test_models.py
 ┃ ┃ ┣ test_views.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ product_management - contains the global settings and configurations for the Django project.
 ┃ ┣ __pycache__
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ templates - contains all the HTML templates for rendering the UI of your application. It's organized based on the app or feature.
 ┃ ┣ buyer
 ┃ ┃ ┗ view_products.html
 ┃ ┣ product
 ┃ ┃ ┗ product_list.html
 ┃ ┣ registration
 ┃ ┃ ┣ create_user.html
 ┃ ┃ ┣ login.html
 ┃ ┃ ┗ signup.html
 ┃ ┣ supplier
 ┃ ┃ ┣ add_product.html
 ┃ ┃ ┣ cheaper_analogues.html
 ┃ ┃ ┣ delete_product.html
 ┃ ┃ ┣ edit_product.html
 ┃ ┃ ┗ view_products.html
 ┃ ┣ base.html
 ┃ ┣ home.html
 ┃ ┗ list_products.html
 ┣ users - handles the users app, responsible for user authentication, group management, and user-related operations.
 ┃ ┣ management
 ┃ ┃ ┣ commands
 ┃ ┃ ┃ ┣ create_groups.py - Command to create user groups such as "Buyers" and "Suppliers".
 ┃ ┃ ┃ ┗ __init__.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ migrations
 ┃ ┣ tests
 ┃ ┃ ┣ test_auth.py
 ┃ ┃ ┣ test_user_groups.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ forms.py
 ┃ ┣ models.py
 ┃ ┣ signals.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ .env
 ┗ manage.py