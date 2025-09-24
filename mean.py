# Daily closing prices for a stock.
stock_prices = [150, 152, 148, 151, 153, 149, 150]

print('stock_prices:', stock_prices)

print('\nlen(stock_prices):', len(stock_prices))

# Calculate the mean/average.
mean_stock_price = sum(stock_prices) / len(stock_prices)

# F-string
# Inside of the curly braces, a variable is being inserted.
print(f'\nMean (Average) Stock Price: {mean_stock_price:.2f}')