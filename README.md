# Ecommerce_Website_Django 


## Project Overview
This repository contains two Django applications: `account` and `product`. The `account` app is responsible for user authentication, registration, and profile management. On the other hand, the `product` app handles product management, including listing products, displaying product details, and managing a user's shopping cart.

## account App
### Forms
#### `forms.py`
The `forms.py` file in the `account` app contains three forms: `AccountAuthenticationForm`, `RegistrationForm`, and `AccountUpdateForm`. These forms are designed for user authentication, registration, and updating user profiles, respectively.

- **`AccountAuthenticationForm`**: Handles user login authentication.
- **`RegistrationForm`**: Manages user registration and includes custom validation for unique email and username.
- **`AccountUpdateForm`**: Allows users to update their account information and profile image.

### Models
#### `models.py`
The `models.py` file defines the data models for the `account` app.

- **`HomePage`**: Represents the homepage content, including contact information and service details.
- **`MyAccountManager`**: Custom manager for the user model (`Account`).
- **`Account`**: Custom user model that extends Django's `AbstractBaseUser`. It includes fields for email, username, profile image, and additional user-related information.

### Views
#### `views.py`
The `views.py` file contains several views for the `account` app, including:

- **`home`**: Renders the homepage.
- **`login_view`**: Manages user login functionality.
- **`register_view`**: Handles user registration.
- **`logout_view`**: Logs out the user.
- **`edit_account_view`**: Allows users to edit their account information.

## product App
### Models
#### `models.py`
The `models.py` file in the `product` app defines data models related to product management.

- **`Category`**: Represents product categories.
- **`Product`**: Defines the product model, including title, description, price, quantity, category, and product image.
- **`Order`**: Represents an order made by a user.
- **`OrderItem`**: Represents an item within an order.
- **`Cart`**: Represents a user's shopping cart.
- **`Payment`**: Represents payment details for an order.

### Views
#### `views.py`
The `views.py` file contains views related to product management, including:

- **`view_product`**: Displays a list of products.
- **`product_detail`**: Displays detailed information about a specific product.
- **`add_to_cart`**: Handles adding products to the user's shopping cart.
- **`checkout`**: Displays the user's shopping cart and total price.
- **`update_cart`**: Updates the quantity of items in the user's shopping cart.

## How to Run the Project
1. Clone the repository: `git clone [repository_url]`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Apply database migrations: `python manage.py migrate`
4. Create a superuser for the Django admin: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`

Now, you can access the Django admin at `http://localhost:8000/admin/` and the applications at their respective URLs.

Feel free to explore the `account` and `product` apps for detailed functionality and customization options.
