# This script reads a CSV file named "sales_data.csv",
# computes total revenue for each product, and writes
# the results into "revenue_summary.csv".

import csv

# Dictionary to store total revenue for each product
revenue = {}

# Read data from the input CSV file
with open("sales_data.csv", "r") as f:
  reader = csv.DictReader(f)

  # Loop through each row of the CSV file
  for row in reader:
    product = row["product"]
    quantity = int(row["quantity"])
    price = float(row["price"])

    # Compute revenue for this row
    total = quantity * price

    # Add to existing revenue for that product
    if product in revenue:
      revenue[product] += total
    else:
      revenue[product] = total

# Write the results to a new CSV file
with open("revenue_summary.csv", "w", newline="") as f:
  writer = csv.writer(f)
  # Write the header row
  writer.writerow(["product", "total_revenue"])

  # Write each product and its total revenue
  for product, total in revenue.items():
    # Rounded for clarity
    writer.writerow([product, round(total, 2)])

print("Revenue summary written to 'revenue_summary.csv'.")