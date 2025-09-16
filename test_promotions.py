from product_classes import Product
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

def test_percent_discount():
    product = Product("Test Product", price=100, quantity=10)
    promo = PercentDiscount("30% off!", percent=30)
    product.promotion = promo  # Property verwenden

    total = product.buy(2)
    # 2 * 100 = 200 → -30% = 140
    assert total == 140
    assert product.quantity == 8  # Menge korrekt reduziert

def test_second_half_price():
    product = Product("Test Product", price=100, quantity=10)
    promo = SecondHalfPrice("Second Half price!")
    product.promotion = promo  # Property verwenden

    total = product.buy(2)
    # First = 100, second = 50 → total = 150
    assert total == 150
    assert product.quantity == 8  # Menge korrekt reduziert

def test_third_one_free():
    product = Product("Test Product", price=100, quantity=10)
    promo = ThirdOneFree("Third One Free!")
    product.promotion = promo  # Property verwenden

    total = product.buy(3)
    # Pay for 2, get 1 free → 200
    assert total == 200
    assert product.quantity == 7  # Menge korrekt reduziert
