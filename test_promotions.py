import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def test_percent_discount():
    product = Product("Test Product", price=100, quantity=10)
    promo = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promo)

    total = product.buy(2)
    # 2 * 100 = 200 → -30% = 140
    assert total == 140


def test_second_half_price():
    product = Product("Test Product", price=100, quantity=10)
    promo = SecondHalfPrice("Second Half price!")
    product.set_promotion(promo)

    total = product.buy(2)
    # First = 100, second = 50 → total = 150
    assert total == 150


def test_third_one_free():
    product = Product("Test Product", price=100, quantity=10)
    promo = ThirdOneFree("Third One Free!")
    product.set_promotion(promo)

    total = product.buy(3)
    # Pay for 2, get 1 free → 200
    assert total == 200
