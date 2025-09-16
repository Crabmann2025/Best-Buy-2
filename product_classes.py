from typing import Optional
from promotions import Promotion


class Product:
    """
    A class to represent a product in a store.
    Supports promotions and price comparisons.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
                Initialize a Product instance.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = quantity > 0
        self._promotion: Optional["Promotion"] = None  # Forward Reference als String


    # Properties
    @property
    def name(self) -> str:
        """Get the product name."""
        return self._name

    @property
    def price(self) -> float:
        """Get the product price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """
            Set the product price.
        """
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def quantity(self) -> int:
        """Get the available stock quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """
            Set the stock quantity and update active status.
        """
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        self._active = value > 0

    @property
    def is_active(self) -> bool:
        """Check if the product is active (available in stock)."""
        return self._active

    @property
    def promotion(self) -> Optional["Promotion"]:
        """Get the promotion assigned to the product, if any."""
        return self._promotion

    @promotion.setter
    def promotion(self, promo: "Promotion"):
        """Assign a promotion to the product."""
        self._promotion = promo


    # Magic Methods
    def __str__(self):
        """
            Return a string representation of the product, including promotion if available.
        """
        base = f"{self.name}, Price: ${self.price} Quantity: {self.quantity}"
        if self.promotion:
            base += f", Promotion: {self.promotion.name}"
        return base

    def __gt__(self, other):
        """
            Compare products by price (greater than).
        """
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        """
            Compare products by price (less than).
        """
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented


    # Buying
    def buy(self, requested_quantity: int) -> float:
        """
            Buy a certain quantity of the product, applying promotion if available.
        """
        if requested_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if requested_quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, requested_quantity)
        else:
            total_price = requested_quantity * self.price

        self.quantity -= requested_quantity
        return total_price


class NonStockedProduct(Product):
    """Represents a product that is not physically stocked (e.g., software licenses)."""

    def __init__(self, name: str, price: float):
        """
            Initialize a NonStockedProduct with zero stock.
        """
        super().__init__(name, price, quantity=0)

    @property
    def quantity(self) -> int:
        """Non-stocked products always have quantity zero."""
        return 0

    @quantity.setter
    def quantity(self, value):
        """Prevent setting quantity for non-stocked products."""
        raise ValueError("Non-stocked products do not track quantity.")

    def buy(self, requested_quantity: int) -> float:
        """
            Buy a certain quantity of a non-stocked product.
        """
        if requested_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        return requested_quantity * self.price


class LimitedProduct(Product):
    """Represents a product with a maximum purchase limit per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
            Initialize a LimitedProduct.
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum per order must be greater than 0.")
        self.maximum = maximum

    def buy(self, requested_quantity: int) -> float:
        """
            Buy a certain quantity of the limited product.
        """
        if requested_quantity > self.maximum:
            raise ValueError(
                f"You can only buy up to {self.maximum} of {self.name} per order."
            )
        return super().buy(requested_quantity)

