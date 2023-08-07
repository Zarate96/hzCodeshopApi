# your_app/tests/test_models.py

import pytest
from django.contrib.auth.models import User
from core.models import Product

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def product(user):
    return Product.objects.create(
        user=user,
        name='Test Product',
        brand='Test Brand',
        category='Test Category',
        description='Test Description',
        rating=4.5,
        numReviews=10,
        price=99.99,
        countInStock=50,
    )

@pytest.mark.django_db
def test_product_name(product):
    assert product.name == 'Test Product'

@pytest.mark.django_db
def test_product_brand(product):
    assert product.brand == 'Test Brand'

@pytest.mark.django_db
def test_product_category(product):
    assert product.category == 'Test Category'

@pytest.mark.django_db
def test_product_rating(product):
    assert product.rating == 4.5

# Add more test functions as needed for other fields and model behavior.
