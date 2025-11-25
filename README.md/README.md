# 🛒 E-Commerce Sales Analysis & Tableau Dashboard
This end-to-end project analyzes e-commerce sales data using Python and visualizes key business metrics through a professional interactive Tableau dashboard. The goal is to derive actionable insights about customer behavior, product performance, and return patterns.

# 🚀 **Project Workflow**

## 1️⃣ Data Cleaning & Transformation (Python)
Performed in `main.py`:

- Merged multiple datasets  
- Standardized column names  
- Cleaned missing values  
- Converted numerical types  
- Added calculated fields:  
  - `amount = discounted_price * quantity`
- Simulated additional fields:  
  - `order_date`
  - `payment_method`
  - `returned_flag`
- Saved final dataset → `orders_final.csv`

---

## 2️⃣ Exploratory Data Analysis (Python)
Performed in `eda_analysis.py`:

- Dataset overview  
- Category-wise revenue  
- Return rate analysis  
- Payment method distribution  
- Monthly sales trend (Matplotlib)  
- Key business insights printed to console  

---

## 3️⃣ Tableau Dashboard (Interactive BI)

### ✔ KPI Cards
- **Total Revenue**
- **Total Orders (Distinct)**
- **Total Customers (Distinct)**
- **Average Order Value (AOV)**

### ✔ Sales & Trend Charts
- Monthly Sales Trend  
- Sales by Country  
- Sales by Category  
- Sales by Payment Mode  
- Top 10 Products  
- Return Rate by Category  

### ✔ Customer Segmentation
- K-Means clustering based on:  
  - Age  
  - Revenue contributed  
  - Order count  
- Cluster labels added to dashboard

---

# 📊 **Final Dashboard (Tableau)**
**Ecommerce_Dashboard.twbx**

This packaged workbook contains:
- Workbook  
- Fully working dashboard  

## 📸 Dashboard Preview
https://github.com/Priyanshuchakraborty14/E-commerce-Data-Analysis/blob/main/Tableau_dashboard/E-Commerce%20Sales%20Performance%20Dashboard.png


# 🔍 **Key Insights**

- **Electronics** contributes the most revenue but has a **higher return rate**.  
- **UPI** is the most preferred payment method.  
- **Top 20% customers contribute ~60% of total revenue**.  
- Monthly sales show seasonal spikes, especially during the festival season.  
- Customer segmentation reveals **3–4 buying clusters** with distinct purchase behaviors.

---

# 🧠 **Skills Demonstrated**

### 📌 Data Skills
- Data Cleaning & Preprocessing  
- Merging large datasets  
- Feature Engineering  
- EDA & Visualization  
- Customer Segmentation  

### 📌 Dashboarding
- KPI Design  
- Trend & Performance Charts  
- Filters, Parameters, Clustering  
- Interactive Tableau Dashboard  

### 📌 Technical Stack
- **Python:** Pandas, NumPy, Matplotlib, Seaborn  
- **Tableau:** Visual Analytics, KPIs, Filters, Clustering  
- **CSV Data Processing**

---

# 📥 **How to Use**
1. Open `/data/orders_final.csv` (final dataset)  
2. Import into Tableau  
3. Open `Ecommerce_Dashboard.twbx` to view final dashboard  
4. Run `eda_analysis.py` for insights  
5. Run `main.py` to regenerate dataset  

---

**Priyanshu Chakraborty**
Data Analyst • Python • SQL • Tableau 