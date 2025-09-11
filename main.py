from products import Product
from store import Store

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    print("--------------------------")

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    active_products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    total_order_price = best_buy.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Total order cost: {total_order_price} dollars.")
