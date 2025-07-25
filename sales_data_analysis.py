sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

for quarter, months in sales_data:
    total = sum(sale for _, sale in months)
    print(f"{quarter} Total Sales: {total}")

all_months = [(month, sale) for _, months in sales_data for month, sale in months]
highest_month = max(all_months, key=lambda x: x[1])
print(f"Highest Sales Month: {highest_month[0]} with {highest_month[1]}")

print("Flat Monthly Sales List:")
print(all_months)

for quarter, months in sales_data:
    for month, sale in months:
        print(f"{quarter} - {month}: {sale}")
