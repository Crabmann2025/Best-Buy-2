class Product:
    """
    A class to represent a product in a store.

    Attributes:
        name (str): The name of the product.
        price (float): Price of the product. Must be >= 0.
        quantity (int): Available quantity. Must be >= 0.
        active (bool): Whether the product is active in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a product instance with validation.
        """
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

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product.
        Automatically deactivates if quantity is 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Prints the product details in a readable format."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, requested_quantity: int) -> float:
        """
        Purchases a specified quantity of the product.

        Args:
            requested_quantity (int): Number of items to buy.

        Returns:
            float: Total price for the purchased items.
        """
        if requested_quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if requested_quantity > self.get_quantity():
            raise ValueError("Not enough stock available.")

        total_price = requested_quantity * self.price
        self.set_quantity(self.get_quantity() - requested_quantity)
        return total_price
