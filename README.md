# Store API

A Django REST API project implementing Clean Architecture principles for a store management system.


## 🏗 Project Structure

```
store_api/
│
├── manage.py
├── requirements.txt
│
├── core/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   ├── category.py
│   │   │   └── product.py
│   │   └── interfaces/
│   │       ├── __init__.py
│   │       ├── category_repository.py
│   │       └── product_repository.py
│   │
│   ├── application/
│   │   ├── __init__.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   └── cache_service.py
│   │   ├── dto/
│   │   │   ├── __init__.py
│   │   │   ├── category_dto.py
│   │   │   └── product_dto.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       ├── category_use_cases.py
│   │       └── product_use_cases.py
│   │
│   └── infrastructure/
│       ├── __init__.py
│       ├── django/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── repositories/
│       │       ├── __init__.py
│       │       ├── category_repository.py
│       │       └── product_repository.py
│       └── cache/
│           ├── __init__.py
│           └── redis_cache_service.py
│
├── api/
│   ├── __init__.py
│   ├── serializers/
│   │   ├── __init__.py
│   │   ├── category_serializer.py
│   │   └── product_serializer.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── category_views.py
│   │   └── product_views.py
│   └── filters/
│       ├── __init__.py
│       └── product_filters.py
│
└── store/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


## 🚀 Features

- Clean Architecture implementation
- REST API endpoints for products and categories
- Database seeding functionality
- Comprehensive DTOs and Repository patterns
- Django REST Framework integration

## 🔧 Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd storeApi
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Seed the database (optional):
```bash
python manage.py seed_db --products n # n is the number of products to create
```

6. Run redis server (optional):
```bash
redis-server

#brew services start redis ( with brew)
```

## 🏃‍♂️ Running the Application
1. Start redis server:
```bash
redis-server
#brew services start redis ( with brew)
```
1. Start the Django server:
```bash
python manage.py runserver
#The API will be available at http://localhost:8000/
```

## 🔍 API Endpoints
### Products
- GET /api/products/ - List all products
- GET /api/products/?category={categoryName} - Filter products by category
- GET /api/products/?price_min={minPrice}&price_max={maxPrice} - Filter products by price range
- GET /api/products/{id}/ - Get product details
- POST /api/products/ - Create a new product
- PUT /api/products/{id}/ - Update a product
- DELETE /api/products/{id}/ - Delete a product
  
### Categories
- GET /api/categories/ - List all categories
- GET /api/categories/{id}/ - Get category details
- POST /api/categories/ - Create a new category
- PUT /api/categories/{id}/ - Update a category
- DELETE /api/categories/{id}/ - Delete a category

## 🏛 Architecture
This project follows Clean Architecture principles:

1. Core Layer
    - Domain Entities
    - Use Cases
    - Repository Interfaces
2. Infrastructure Layer
    - Django Models
    - Database Implementation
    - External Services
3. Interface Layer
    - REST API Controllers
    - Serializers
    - DTOs