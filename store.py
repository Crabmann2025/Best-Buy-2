from typing import List, Tuple
from product_classes import Product


class Store:
    """
        A store containing products. Supports product management, ordering,
        and several magic methods for convenience.
    """

    def __init__(self, product_list: List[Product] = None):
        """ Initialize a Store instance with an optional list of products."""
        self.products = product_list if product_list else []

    # Order processing as static method
    @staticmethod
    def order(shopping_list: List[Tuple[Product, int]]) -> float:
        """
            Process an order given a shopping list of products and quantities.
        """
        total = 0.0
        for product, qty in shopping_list:
            total += product.buy(qty)
        return total

    # Product management
    def add_product(self, product: Product):
        """
            Add a product to the store if it doesn't already exist.
        """
        if any(p.name == product.name for p in self.products):
            print(f"Product '{product.name}' already exists in the store.")
        else:
            self.products.append(product)

    def remove_product(self, product: Product):
        """
            Remove a product from the store.
        """
        for p in self.products:
            if p.name == product.name:
                self.products.remove(p)
                return
        print(f"Product '{product.name}' not found in the store.")

    def get_total_quantity(self) -> int:
        """
            Get the total quantity of all active products in the store.
        """
        return sum(p.quantity for p in self.products if p.is_active)

    def get_all_products(self) -> List[Product]:
        """
            Get a list of all active products in the store.
        """
        return [p for p in self.products if p.is_active]


    # Magic methods
    def __contains__(self, item):
        """ Check if a product is in the store."""
        return item in self.products

    def __add__(self, other):
        """
            Combine two stores into a new store containing all products.
        """
        if isinstance(other, Store):
            combined_products = self.products + other.products
            return Store(combined_products)
        return NotImplemented

    def __str__(self):
        """ Return a string representation of all products in the store."""
        return "\n".join(str(p) for p in self.products)
