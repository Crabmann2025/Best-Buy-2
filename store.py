from typing import List, Tuple
import products  # make sure products.py is in the same folder

class Store:
    """
    A class to represent a store that holds multiple products.

    Attributes:
        products (List[products.Product]): List of Product instances available in the store.
    """

    def __init__(self, product_list: List[products.Product]):
        """
        Initializes the store with a list of products.

        Args:
            product_list (List[products.Product]): Initial list of products for the store.
        """
        self.products = product_list

    def add_product(self, product: products.Product):
        """
        Adds a product to the store.

        Args:
            product (products.Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """
        Removes a product from the store if it exists.

        Args:
            product (products.Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all active products in the store.

        Returns:
            int: Total number of items available in the store.
        """
        total = sum(product.get_quantity() for product in self.products if product.is_active())
        return total

    def get_all_products(self) -> List[products.Product]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[products.Product]: Active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Processes an order consisting of multiple products and quantities.

        Args:
            shopping_list (List[Tuple[products.Product, int]]): A list of tuples, each containing
            a Product and the quantity to purchase.

        Returns:
            float: Total price of the order.
        """
        total_price = 0.0
        for item, quantity in shopping_list:
            if item.is_active():
                try:
                    total_price += item.buy(quantity)
                except ValueError as e:
                    print(f"Cannot buy {quantity} of {item.name}: {e}")
            else:
                print(f"Product {item.name} is inactive and cannot be ordered.")
        return total_price
