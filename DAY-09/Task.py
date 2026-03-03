import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("Coffee Shop Sales.csv")

# Clean column names
data.columns = data.columns.str.strip().str.lower()

# Create Pivot Table (Total Quantity per Product)
purchase_df = data.pivot_table(
    values="transaction_qty",
    index="product_type",
    aggfunc="sum"
)

# Sort from highest to lowest
purchase_df = purchase_df.sort_values(by="transaction_qty", ascending=False)

# Top 5 Most Purchased
top5 = purchase_df.head(5)

# Top 5 Least Purchased
bottom5 = purchase_df.tail(5)

print("\nTop 5 Most Purchased Products:")
print(top5)

print("\nTop 5 Least Purchased Products:")
print(bottom5)

# Plot Top 5 Chart
top5.plot(kind="bar", legend=False)
plt.title("Top 5 Most Purchased Products")
plt.xlabel("Product Type")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Bottom 5 Chart
bottom5.plot(kind="bar", legend=False)
plt.title("Top 5 Least Purchased Products")
plt.xlabel("Product Type")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
