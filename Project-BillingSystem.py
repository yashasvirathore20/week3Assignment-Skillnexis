class Product:
    def __init__(self):
        self.name = input("Enter name of the product: ")
        self.price = int(input("Enter price: "))
        self.quantity = int(input("Enter quantity: "))

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.tax_rate = 10
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        subtotal = 0
        print("\n" + "=" * 40)
        print(f"{'Item':<15} {'Price':<8} {'Qty':<5} {'Total':<8}")
        print("-" * 40)

        for p in self.products:
            total = p.get_total()
            subtotal += total
            print(f"{p.name:<15} {p.price:<8} {p.quantity:<5} {total:<8}")

        tax = subtotal * (self.tax_rate / 100)
        grand_total = subtotal + tax

        print("-" * 40)
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Tax ({self.tax_rate}%): {tax:.2f}")
        print(f"Grand Total: {grand_total:.2f}")
        print("=" * 40)


bill = Bill()
bill.add_product(Product())
bill.add_product(Product())
bill.display_bill()