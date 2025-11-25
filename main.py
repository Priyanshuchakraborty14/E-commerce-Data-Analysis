# ===============================================
# E-Commerce Project - Clean Merge & Simulation
# ===============================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# -----------------------------
# 1. Load Datasets
# -----------------------------
print(f"📁 Current directory: {os.getcwd()}")
try:
    print(f"📂 Files in data folder: {os.listdir('data')}")
except FileNotFoundError:
    print("⚠️ 'data' folder not found. Ensure the path is correct.")

flipkart = pd.read_csv("data/flipkart_com-ecommerce_sample.csv")
ecommerce = pd.read_csv("data/ecommerce_dataset_10000.csv")

print("✅ Files loaded successfully!\n")

# -----------------------------
# 2. Inspect Columns
# -----------------------------
print("--- Flipkart Dataset Columns ---")
print(list(flipkart.columns))
print("\n--- Ecommerce Dataset Columns ---")
print(list(ecommerce.columns))

# -----------------------------
# 3. Standardize Column Names
# -----------------------------
flipkart.rename(columns={
    'pid': 'product_id',
    'product_category_tree': 'category',
    'retail_price': 'retail_price',
    'discounted_price': 'discounted_price'
}, inplace=True)

ecommerce.rename(columns={
    'product_id': 'product_id',
    'unit_price': 'unit_price'
}, inplace=True)

print("\n✅ After renaming columns:")
print("Flipkart Columns:", list(flipkart.columns))
print("Ecommerce Columns:", list(ecommerce.columns))

# -----------------------------
# 4. Convert Numeric Columns
# -----------------------------
for col in ['retail_price', 'discounted_price', 'unit_price']:
    if col in flipkart.columns:
        flipkart[col] = pd.to_numeric(flipkart[col], errors='coerce')
    if col in ecommerce.columns:
        ecommerce[col] = pd.to_numeric(ecommerce[col], errors='coerce')

# -----------------------------
# 5. Handle Missing Values
# -----------------------------
flipkart.dropna(subset=['product_id'], inplace=True)
ecommerce.dropna(subset=['customer_id', 'product_id'], inplace=True)
ecommerce['quantity'] = ecommerce['quantity'].fillna(1) 

# -----------------------------
# 6. Merge Datasets
# -----------------------------
orders = ecommerce.merge(
    flipkart[['product_id', 'category', 'brand', 'retail_price', 'discounted_price']],
    on='product_id',
    how='left'
)

# -----------------------------
# 7. Clean Merge Duplicates
# -----------------------------
orders.rename(columns={'category_y': 'category'}, inplace=True)
orders['category'] = orders['category'].fillna(orders['category_x'])

if 'retail_price' in orders.columns and 'unit_price' in orders.columns:
    orders['retail_price'] = orders['retail_price'].fillna(orders['unit_price'])
if 'discounted_price' in orders.columns and 'retail_price' in orders.columns:
    orders['discounted_price'] = orders['discounted_price'].fillna(orders['retail_price'])

orders.drop(columns=[col for col in orders.columns if col.endswith('_x') or col.endswith('_y')],
            inplace=True, errors='ignore')

# -----------------------------
# 8. Add Calculated Fields
# -----------------------------
orders['amount'] = orders['discounted_price'] * orders['quantity']

# -----------------------------
# 9. Simulate Missing Data (Dates, Payment, Returns)
# -----------------------------
def random_date(start, end, n):
    return [start + timedelta(days=random.randint(0, (end-start).days)) for _ in range(n)]

orders['order_date'] = random_date(datetime(2021,1,1), datetime(2023,12,31), len(orders))

payment_methods = ['UPI', 'Card', 'COD']
orders['payment_method'] = np.random.choice(payment_methods, size=len(orders), p=[0.6, 0.3, 0.1])

orders['category'] = orders['category'].astype(str)

category_return_prob = {'Electronics': 0.1, 'Fashion': 0.05, 'Home & Kitchen': 0.03, 'Books': 0.02}
default_prob = 0.04
orders['returned_flag'] = orders['category'].apply(
    lambda x: np.random.choice([0, 1], p=[1 - category_return_prob.get(x, default_prob),
                                          category_return_prob.get(x, default_prob)])
)

# -----------------------------
# 10. Save Final Dataset
# -----------------------------
output_file = "data/orders_final.csv"

# 🧹 Drop the empty 'brand' column before saving
orders.drop(columns=['brand'], inplace=True, errors='ignore')

orders.to_csv(output_file, index=False)
print(f"\n✅ Final dataset saved as '{output_file}' with {len(orders)} records")

# -----------------------------
# 11. Preview Final Data
# -----------------------------
print("\n--- Sample of Final Orders Data ---")
print(orders.head())
