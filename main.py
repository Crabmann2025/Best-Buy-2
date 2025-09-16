from product_classes import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


def show_menu():
    """
        Display the main menu options to the user.
    """
    print("\nWelcome to the Store!")
    print("1. List all products")
    print("2. Show total stock quantity")
    print("3. Make an order")
    print("4. Quit")


def handle_list_products(store: Store):
    """
        Print all products available in the store.
    """
    print("\nAvailable products:")
    for p in store.get_all_products():
        print(p)


def handle_total_quantity(store: Store):
    """
        Print the total quantity of all products in the store.
    """
    print(f"\nTotal quantity in store: {store.get_total_quantity()}")


def handle_order(store: Store):
    """
        Handle the order process by allowing the user to select products
        and quantities, then calculate the total cost.
    """
    shopping_list = []
    while True:
        product_name = input("\nEnter product name (or 'done' to finish): ").strip()
        if product_name.lower() == "done":
            break

        product = next(
            (p for p in store.get_all_products() if p.name.lower() == product_name.lower()), None
        )
        if not product:
            print("Product not found.")
            continue

        try:
            qty = int(input(f"Enter quantity of '{product.name}': "))
            if qty <= 0:
                print("Quantity must be positive!")
                continue
            shopping_list.append((product, qty))
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"\nOrder processed. Total cost: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Order failed: {e}")
    else:
        print("No items ordered.")


def start(store: Store):
    """
        Start the main store interaction loop.
    """
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_list_products(store)
        elif choice == "2":
            handle_total_quantity(store)
        elif choice == "3":
            handle_order(store)
        elif choice == "4":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    """
       Initialize products, assign promotions, create a store, and start the interaction loop.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Promotions
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Assign promotions
    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent

    store = Store(product_list)
    start(store)


if __name__ == "__main__":
    main()