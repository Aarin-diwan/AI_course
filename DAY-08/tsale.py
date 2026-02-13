import pandas as pd
d = pd.read_csv("coffee_shop_sales.csv")
d["total_price"] = d["transaction_qty"] * d["unit_price"]
tsales = 0
tsales += d["total_price"]
print(tsales)
print(d.head())
