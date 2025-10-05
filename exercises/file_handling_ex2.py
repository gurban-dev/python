'''
Scenario:
You have a CSV file sales_data.csv that tracks
sales transactions for a small store:

date,product,quantity,price
2025-10-01,Apple,10,0.5
2025-10-01,Banana,5,0.3
2025-10-02,Apple,7,0.5
2025-10-02,Banana,8,0.3

Task:
1. Read the CSV file.

2. Compute the total revenue per product (quantity x
   price summed across all days).

3. Write the results to a new CSV file revenue_summary.csv like:

   product,total_revenue
   Apple,8.5
   Banana,3.9

Hints:
Use the csv module (csv.reader and csv.writer).

A dictionary can help store running totals per product.

Remember to convert strings from the CSV to numbers (int or float).
'''