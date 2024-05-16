import pandas as pd 

print("Q3 Execution Started!!!!")   
data = pd.read_excel('Q3.xlsx')

min_date,max_date,sales=data["Date"].min(),data["Date"].max(),data["Sales"]

data = {
    "Date": pd.date_range(start=min_date, end=max_date),
    "Sales":sales
}

df = pd.DataFrame(data)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()

monthly_sales = df.groupby(['Year', 'Month'])
monthly_sales=monthly_sales['Sales'].sum().unstack()

months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
sorted_columns = sorted(monthly_sales.columns, key=lambda x: months_order.index(x))

monthly_sales=monthly_sales[sorted_columns]

monthly_sales.to_excel("Q3_output.xlsx")
print("Q3 Execution Completed..Check Q3_output.xlsx file")