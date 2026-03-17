monthly_sales = (15000, 12000, 18000, 16500, 21000, 19500, 22000, 24000, 20000, 17500, 23000, 25000)
print("Monthly sales figures:")
for month_num, sales in enumerate(monthly_sales, 1):
    print(f"Month {month_num}: ${sales:,.2f}")
total_annual_sales = sum(monthly_sales)
print("\nTotal annual sales:")
print(f"${total_annual_sales:,.2f}")
