import pytest
from products import Product  # Import your Product class


def test_create_product_success():
    """Test that creating a valid product works."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active() is True


def test_create_product_invalid_name():
    """Test that an empty product name raises an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_invalid_price():
    """Test that a negative price raises an exception."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_zero():
    """Test that a product becomes inactive when its quantity reaches 0."""
    p = Product("Mouse", price=50, quantity=1)
    p.buy(1)
    assert p.get_quantity() == 0
    assert p.is_active() is False


def test_product_buy_reduces_quantity():
    """Test that buying a product reduces its quantity and returns the total price."""
    p = Product("Keyboard", price=100, quantity=5)
    total = p.buy(2)
    assert total == 200
    assert p.get_quantity() == 3


def test_product_buy_too_much_raises():
    """Test that buying more items than available raises an exception."""
    p = Product("Headphones", price=300, quantity=2)
    with pytest.raises(ValueError):
        p.buy(5)
