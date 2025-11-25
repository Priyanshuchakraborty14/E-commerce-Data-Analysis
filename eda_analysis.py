# ===============================================
# 🧠 E-Commerce Exploratory Data Analysis (EDA)
# ===============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1️⃣ Load Final Dataset
# -----------------------------
orders = pd.read_csv("data/orders_final.csv")

# -----------------------------
# 2️⃣ Basic Data Overview
# -----------------------------
print("\n📊 Dataset Info:")
print(orders.info())

print("\n🔍 Missing Values:")
print(orders.isnull().sum())

print("\n💰 Sales Summary:")
print(orders['amount'].describe())

print("\n📦 Category-wise Sales:")
print(orders.groupby('category')['amount'].sum().sort_values(ascending=False))

print("\n🔁 Return Rate by Category:")
print(orders.groupby('category')['returned_flag'].mean().sort_values(ascending=False))

print("\n💳 Payment Method Distribution:")
print(orders['payment_method'].value_counts(normalize=True) * 100)

# -----------------------------
# 3️⃣ Visualization Section
# -----------------------------
# Total Sales by Category
plt.figure(figsize=(8,4))
sns.barplot(x='category', y='amount', data=orders, estimator='sum', ci=None)
plt.title("💰 Total Sales by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Return Rate by Category
plt.figure(figsize=(8,4))
sns.barplot(x='category', y='returned_flag', data=orders, estimator='mean', ci=None)
plt.title("🔁 Return Rate by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 4️⃣ Business Insights
# -----------------------------
print("\n📈 Business Insights:")
print("- Top performing category:", orders.groupby('category')['amount'].sum().idxmax())
print("- Category with highest return rate:", orders.groupby('category')['returned_flag'].mean().idxmax())
print("- Most preferred payment method:", orders['payment_method'].mode()[0])
print("- Average order value (AOV): ₹", round(orders['amount'].mean(), 2))
print("- Total revenue generated: ₹", round(orders['amount'].sum(), 2))

# -----------------------------
# 5️⃣ Monthly Sales Trend
# -----------------------------
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
monthly_sales = orders.groupby(orders['order_date'].dt.to_period('M'))['amount'].sum()

plt.figure(figsize=(10,4))
monthly_sales.plot(kind='line', marker='o', title='📅 Monthly Sales Trend', color='tab:blue')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.tight_layout()
plt.show()
