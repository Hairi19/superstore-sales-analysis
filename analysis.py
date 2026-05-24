import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv(r'C:\portfolio\project1\train.csv', encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

print("✅ Data loaded successfully!")
print(f"Total Orders: {df.shape[0]}")
print(f"Total Sales Revenue: ${df['Sales'].sum():,.2f}")
print(f"Average Order Value: ${df['Sales'].mean():,.2f}")

# ── Chart 1: Sales by Category ─────────────────────────
plt.figure(figsize=(8,5))
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
sns.barplot(x=category_sales.values, y=category_sales.index, palette='Blues_d')
plt.title('Total Sales by Category', fontsize=14)
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig(r'C:\portfolio\project1\chart1_category_sales.png')
plt.show()
print("✅ Chart 1 saved!")

# ── Chart 2: Sales by Region ───────────────────────────
plt.figure(figsize=(8,5))
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
sns.barplot(x=region_sales.values, y=region_sales.index, palette='Greens_d')
plt.title('Total Sales by Region', fontsize=14)
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig(r'C:\portfolio\project1\chart2_region_sales.png')
plt.show()
print("✅ Chart 2 saved!")

# ── Chart 3: Monthly Sales Trend ──────────────────────
plt.figure(figsize=(10,5))
monthly = df.groupby(['Year','Month'])['Sales'].sum().reset_index()
monthly['Date'] = pd.to_datetime(monthly[['Year','Month']].assign(Day=1))
plt.plot(monthly['Date'], monthly['Sales'], marker='o', color='steelblue')
plt.title('Monthly Sales Trend Over Time', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(r'C:\portfolio\project1\chart3_monthly_trend.png')
plt.show()
print("✅ Chart 3 saved!")

# ── Chart 4: Top 10 Sub-Categories ────────────────────
plt.figure(figsize=(8,6))
top_sub = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_sub.values, y=top_sub.index, palette='Oranges_d')
plt.title('Top 10 Sub-Categories by Sales', fontsize=14)
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig(r'C:\portfolio\project1\chart4_subcategory.png')
plt.show()
print("✅ Chart 4 saved!")

print("\n🎉 Analysis complete! All 4 charts saved to your project folder.")