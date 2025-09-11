from products import Product
from store import Store

def start(store: Store):
    """
    Starts the user interface for interacting with the store.

    Args:
        store (Store): The store object containing all products.
    """
    while True:
        print("\nWelcome to the Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nProducts available in the store:")
            for product in store.get_all_products():
                product.show()

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal quantity of all active products: {total_quantity}")

        elif choice == "3":
            print("\nMake your order. Enter product numbers separated by commas.")
            products_list = store.get_all_products()
            for idx, product in enumerate(products_list, start=1):
                print(f"{idx}. {product.name} - Price: {product.price}, Quantity: {product.get_quantity()}")

            order_input = input("Enter product numbers to order (e.g., 1,2): ")
            quantities_input = input("Enter quantities for each product (e.g., 3,5): ")

            try:
                product_indices = [int(x.strip()) - 1 for x in order_input.split(",")]
                quantities = [int(x.strip()) for x in quantities_input.split(",")]

                if len(product_indices) != len(quantities):
                    print("Error: The number of products and quantities must match.")
                    continue

                shopping_list = [(products_list[i], quantities[i]) for i in range(len(product_indices))]
                total_price = store.order(shopping_list)
                print(f"Total order cost: {total_price} dollars.")

            except (ValueError, IndexError) as e:
                print(f"Invalid input: {e}")

        elif choice == "4":
            print("Thank you for visiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    # Start the user interface
    start(best_buy)
