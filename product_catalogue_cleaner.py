products = [
    {"name": "Daal Chana", "price": "280", "category": "Grocery"},
    {"name": "Cooking Oil", "price": 540, "category": "Grocery"},
    {"name": "Lux Soap", "price": "120", "category": "Household"},
    {"name": "Tapal Tea", "price": "350", "category": "Grocery"},
    {"name": "Daal Chana", "price": "280", "category": "Grocery"},
    {"name": "Surf Excel", "price": None, "category": "Household"},
    {"name": "Biscuits", "price": "50", "category": "Snacks"},
]

clean_products = []
seen = set()

for product in products:
    key = (product["name"].strip().lower(), product["category"].strip().lower())
    if key in seen:
        continue
    seen.add(key)

    try:
        price = float(product["price"])
    except (TypeError, ValueError):
        price = 0.0

    clean_products.append({
        "name": product["name"].strip(),
        "price": price,
        "category": product["category"].strip()
    })

by_category = {}
for product in clean_products:
    category = product["category"]
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(product)

print("PRODUCT CATALOGUE SUMMARY")
print("Products after cleaning:", len(clean_products))
for category, items in by_category.items():
    total = sum(item["price"] for item in items)
    print(f"\n{category}: {len(items)} products, total value Rs. {total:.2f}")
    for item in items:
        print(f"  {item['name']}: Rs. {item['price']:.2f}")
