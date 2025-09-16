import pytest
from product_classes import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_create_product_success():
    """Test that creating a valid product works."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active is True  # Property


def test_create_product_invalid_name():
    """Creating a product with empty name should raise ValueError."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_invalid_price():
    """Creating a product with negative price should raise ValueError."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_zero():
    """Product becomes inactive when its quantity reaches 0."""
    p = Product("Mouse", price=50, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert p.is_active is False


def test_product_buy_reduces_quantity():
    """Buying a product reduces its quantity and returns total price."""
    p = Product("Keyboard", price=100, quantity=5)
    total = p.buy(2)
    assert total == 200
    assert p.quantity == 3


def test_product_buy_too_much_raises():
    """Buying more than available quantity raises ValueError."""
    p = Product("Monitor", price=300, quantity=2)
    with pytest.raises(ValueError):
        p.buy(5)


def test_non_stocked_product_buy():
    """NonStockedProduct can always be bought regardless of quantity."""
    p = NonStockedProduct("Windows License", price=125)
    total = p.buy(10)
    assert total == 1250
    assert p.quantity == 0  # quantity is always 0
    assert p.is_active is False  # Non-stocked products are treated as inactive


def test_limited_product_maximum():
    """LimitedProduct cannot be bought above maximum per order."""
    p = LimitedProduct("Shipping", price=10, quantity=10, maximum=2)
    total = p.buy(2)
    assert total == 20
    with pytest.raises(ValueError):
        p.buy(3)


def test_promotions_percent_discount():
    """PercentDiscount applies correct discount."""
    p = Product("Test Product", price=100, quantity=10)
    promo = PercentDiscount("30% off!", percent=30)
    p.promotion = promo
    total = p.buy(2)
    assert total == 140  # 100*2 - 30% = 140


def test_promotions_second_half_price():
    """SecondHalfPrice applies correct pricing."""
    p = Product("Test Product", price=100, quantity=10)
    promo = SecondHalfPrice("Second Half price!")
    p.promotion = promo
    total = p.buy(3)  # 2 full price + 1 half price
    assert total == 250  # 100+100+50


def test_promotions_third_one_free():
    """ThirdOneFree applies correct pricing."""
    p = Product("Test Product", price=100, quantity=10)
    promo = ThirdOneFree("Third One Free!")
    p.promotion = promo
    total = p.buy(3)  # pay for 2, 1 free
    assert total == 200
