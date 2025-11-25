# -----------------------------
# 6. Merge Datasets
# -----------------------------
# Since both DFs have 'category', the result will have 'category_x' (ecommerce) and 'category_y' (flipkart)
orders = ecommerce.merge(
    flipkart[['product_id', 'category', 'brand', 'retail_price', 'discounted_price']],
    on='product_id',
    how='left'
)

# -----------------------------
# 7. Clean Merge Duplicates (FIX for KeyError: 'category' applied here)
# -----------------------------
orders.rename(columns={
    # We choose the more detailed 'category' from flipkart (right DF) and rename it to 'category'
    'category_y': 'category' 
}, inplace=True)

# Fill missing prices (FutureWarning Fix: Use assignment instead of inplace=True)
if 'retail_price' in orders.columns and 'unit_price' in orders.columns:
    orders['retail_price'] = orders['retail_price'].fillna(orders['unit_price'])
if 'discounted_price' in orders.columns and 'retail_price' in orders.columns:
    orders['discounted_price'] = orders['discounted_price'].fillna(orders['retail_price'])

# Remove duplicate suffixes (this deletes the less detailed 'category_x' from ecommerce)
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

# FIX for TypeError: unhashable type: 'Series' and ensuring we use the renamed column
orders['category'] = orders['category'].astype(str)

category_return_prob = {'Electronics': 0.1, 'Fashion': 0.05, 'Home & Kitchen': 0.03, 'Books': 0.02}
default_prob = 0.04
orders['returned_flag'] = orders['category'].apply(
    lambda x: np.random.choice([0, 1], p=[1 - category_return_prob.get(x, default_prob),
                                          category_return_prob.get(x, default_prob)])
)