import os
import django

# Configure Django settings for standalone ORM usage
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Product


def seed_products():
    """
    Populate the database with sample products (UPC, name, price).
    Only runs if there are no products yet, to avoid duplicates.
    """
    if Product.objects.exists():
        print("Products already exist. Skipping seeding.")
        return

    products = [
        # upc, name, price in cents
        ("111111111111", "2L Milk", 399),
        ("222222222222", "Whole Wheat Bread", 299),
        ("333333333333", "Dozen Eggs", 549),
        ("444444444444", "Apples 1kg", 399),
        ("555555555555", "Cheddar Cheese 500g", 749),
    ]

    objs = [
        Product(upc=upc, name=name, price_cents=price_cents)
        for upc, name, price_cents in products
    ]
    Product.objects.bulk_create(objs)

    print("Database populated with sample products.")


def scan_loop():
    """
    Simple cash register 'UI':
    - Prompt for UPC (simulating a scan/input box)
    - Look up via Django ORM
    - Display product name and price
    """
    print("\n=== Cash Register ===")
    print("Enter or scan a UPC code.")
    print("Type 'q' to quit.\n")

    while True:
        upc = input("Scan / Enter UPC: ").strip()

        if upc.lower() == "q":
            print("Exiting cash register.")
            break

        if not upc:
            print("Please enter a UPC.\n")
            continue

        try:
            product = Product.objects.get(upc=upc)
            print(f"Product: {product.name} | Price: ${product.price:.2f}\n")
        except Product.DoesNotExist:
            print("Product not found for this UPC.\n")


if __name__ == "__main__":
    seed_products()
    scan_loop()
