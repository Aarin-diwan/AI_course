import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("coffee_shop_sales.csv")

# 1. Add total_amount column 
data['total_amount'] = data['unit_price'] * data['transaction_qty']

# 2. Find total sales
total_sales = data['total_amount'].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# 3. Most and least purchased products by quantity
product_quantity = data.groupby('product_detail')['transaction_qty'].sum().sort_values(ascending=False)

most_purchased = product_quantity.head(1)
least_purchased = product_quantity.tail(1)

print(f"\nMost Purchased Product: {most_purchased.index[0]} - Quantity: {most_purchased.values[0]}")
print(f"Least Purchased Product: {least_purchased.index[0]} - Quantity: {least_purchased.values[0]}")

print("\n--- Top 5 Most Purchased Products ---")
print(product_quantity.head(5))

print("\n--- Top 5 Least Purchased Products ---")
print(product_quantity.tail(5))

# ----------------- GRAPH -----------------

# Get Top 5 and Bottom 5
top5 = product_quantity.head(5)
bottom5 = product_quantity.tail(5)

plt.figure(figsize=(10,6))

# Combine both
combined = pd.concat([top5, bottom5])

combined.plot(kind='bar')

plt.title("Top 5 and Bottom 5 Purchased Products")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
