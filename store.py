from typing import List, Tuple
from products import Product

class Store:
    """
    A class to represent a store containing multiple products.
    """

    def __init__(self, product_list: List[Product]):
        """
        Initializes the store with a list of products.

        Args:
            product_list (List[Product]): Initial product list.
        """
        if not all(isinstance(p, Product) for p in product_list):
            raise TypeError("All items in product_list must be Product instances.")
        self.products = product_list

    def add_product(self, product: Product):
        """
        Adds a product to the store, ensuring no duplicates by name.
        """
        if any(p.name == product.name for p in self.products):
            print(f"Product '{product.name}' already exists in the store.")
        else:
            self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store if it exists.
        """
        for p in self.products:
            if p.name == product.name:
                self.products.remove(p)
                return
        print(f"Product '{product.name}' not found in the store.")

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all active products."""
        return sum(p.get_quantity() for p in self.products if p.is_active())

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order consisting of multiple products.

        Args:
            shopping_list (List[Tuple[Product, int]]): List of (Product, quantity).

        Returns:
            float: Total cost of the order.
        """
        total = 0
        for product, qty in shopping_list:
            total += product.buy(qty)
        return total
