class Product:
    """
    A class to represent a product in a store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False
        self.promotion = None   # <-- NEW


    # Promotion handling
    def set_promotion(self, promotion):
        """Assign a promotion to this product."""
        self.promotion = promotion

    def get_promotion(self):
        """Return the promotion if set."""
        return self.promotion


    # Core logic
    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}")

    def buy(self, requested_quantity: int) -> float:
        if requested_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if requested_quantity > self.get_quantity():
            raise ValueError("Not enough stock available.")

        # Apply promotion if set
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, requested_quantity)
        else:
            total_price = self.price * requested_quantity

        # Update stock
        self.set_quantity(self.get_quantity() - requested_quantity)
        return total_price



class NonStockedProduct(Product):
    """
    Represents a product that is not physically stocked (e.g., software licenses).
    Quantity is always 0 and cannot be changed.
    """

    def __init__(self, name: str, price: float):
        # Always set quantity = 0
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Non-stocked products cannot change quantity."""
        raise ValueError("Non-stocked products do not track quantity.")

    def get_quantity(self) -> int:
        """Always return 0."""
        return 0

    def buy(self, requested_quantity: int) -> float:
        """
        Non-stocked products can always be purchased, regardless of quantity.
        """
        if requested_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        return requested_quantity * self.price

    def show(self):
        """Show product details with info about being non-stocked."""
        print(f"{self.name}, Price: {self.price}, Non-stocked product (unlimited availability)")


class LimitedProduct(Product):
    """
    Represents a product that can only be purchased up to a maximum per order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum per order must be greater than 0.")
        self.maximum = maximum

    def buy(self, requested_quantity: int) -> float:
        """Ensure purchase does not exceed the maximum allowed per order."""
        if requested_quantity > self.maximum:
            raise ValueError(
                f"You can only buy up to {self.maximum} of {self.name} per order."
            )
        return super().buy(requested_quantity)

    def show(self):
        """Show product details with max-per-order information."""
        print(
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
            f"Max per order: {self.maximum}"
        )




