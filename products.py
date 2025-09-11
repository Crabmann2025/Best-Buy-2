class Product:
    """
    A class to represent a product in a store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity available in stock.
        active (bool): Indicates if the product is active (available for purchase).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): Name of the product.
            price (float): Price of the product. Must be non-negative.
            quantity (int): Quantity of the product. Must be non-negative.

        Raises:
            ValueError: If name is empty or price/quantity is negative.
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
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        Returns:
            int: Quantity available.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the product quantity. Deactivates the product if quantity reaches 0.

        Args:
            quantity (int): New quantity. Must be non-negative.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints the product details in a readable format."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Purchases a specified quantity of the product.

        Args:
            quantity (int): Number of items to buy. Must be positive and not exceed available stock.

        Returns:
            float: Total price of the purchase.

        Raises:
            ValueError: If quantity is invalid or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available for purchase.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        total_price = self.price * quantity
        return total_price
