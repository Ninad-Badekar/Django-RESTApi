
# E-Commerce Project

## Overview
This project is a fully functional e-commerce platform built using Django and Django REST Framework (DRF). It includes modules for user authentication, product management, shopping cart, and order processing.

## Features
- User Registration & JWT Authentication
- Product CRUD Operations
- Shopping Cart Management
- Order Placement & Tracking
- Swagger API Documentation

## Technologies Used
- Python 3.8+
- Django 4.2+
- Django REST Framework
- MySQL
- JWT for Authentication
- Swagger (drf-yasg) for API Documentation
- Pytest for Testing

## Installation
1. Clone the repository:
```
git clone https://github.com/username/ecommerce.git
cd ecommerce
```
2. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Configure database settings in `settings.py`
5. Apply migrations:
```
python manage.py migrate
```
6. Run the development server:
```
python manage.py runserver
```

## Testing
Run tests using Pytest:
```
pytest
```

## API Documentation
Swagger UI is available at:
```
http://localhost:8000/swagger/
```
ReDoc documentation is available at:
```
http://localhost:8000/redoc/
```

## Folder Structure
- `users/` - User authentication & management
- `products/` - Product CRUD operations
- `cart/` - Shopping cart module
- `orders/` - Order placement & tracking
- `Ecommerce/` - Project settings & URLs

