from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
    Abstract base class for all promotions.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculate the price after applying the promotion.
        Must be implemented by all subclasses.
        """
        pass


class PercentDiscount(Promotion):
    """
    Promotion: applies a percentage discount on the total price.
    """

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if percent <= 0 or percent >= 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount


class SecondHalfPrice(Promotion):
    """
    Promotion: buy one, get the second at half price.
    """

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # Every second item is half price
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """
    Promotion: buy 2, get 1 free.
    """

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # For every 3 items, 1 is free
        payable_items = quantity - (quantity // 3)
        return payable_items * product.price
