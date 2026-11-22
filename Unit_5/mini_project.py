# Mini Project: Retail Sales Dashboard

import csv
import os
import matplotlib.pyplot as plt

# Find the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(folder, "sales.csv")

# Create sales CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product", "Quantity", "Price"])
    writer.writerow(["Laptop", 3, 75000])
    writer.writerow(["Mobile", 5, 30000])
    writer.writerow(["Headphones", 3, 10000])
    writer.writerow(["Keyboard", 2, 5000])
    writer.writerow(["Mouse", 2, 5000])

# Read CSV file
products = []
revenue = []

total_sales = 0

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        amount = quantity * price

        products.append(product)
        revenue.append(amount)

        total_sales += amount

# Display Sales Report
print("RETAIL SALES REPORT")
print("------------------")

for i in range(len(products)):
    print(products[i], ":", revenue[i])

print("------------------")
print("Total Sales:", total_sales)

# Create TWO graphs in one window
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Graph 1: Bar Chart
axes[0].bar(products, revenue)

axes[0].set_xlabel("Products")
axes[0].set_ylabel("Revenue")
axes[0].set_title("Product Sales Revenue")
axes[0].tick_params(axis="x", rotation=30)

# Graph 2: Pie Chart
axes[1].pie(
    revenue,
    labels=products,
    autopct="%1.1f%%"
)

axes[1].set_title("Sales Revenue Distribution")

# Main title
fig.suptitle("Retail Sales Dashboard", fontsize=16)

# Adjust layout
plt.tight_layout()

# Display BOTH graphs
plt.show()