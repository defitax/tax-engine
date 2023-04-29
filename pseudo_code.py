#There will be few lists will be added to understand the difference between to two users transactions. This was only the complete of one layer there will be more added and connected with all time line accross the core areas.

# Define the list of sale transactions as a list of dictionaries
sales = [
    {'number_of_coins_sold': 5, 'cost_per_coin_at_purchase': 100, 'selling_price_per_coin': 150},
    {'number_of_coins_sold': 20, 'cost_per_coin_at_purchase': 10, 'selling_price_per_coin': 20},
    {'number_of_coins_sold': 10, 'cost_per_coin_at_purchase': 10, 'selling_price_per_coin': 20},
]

# Create a variable to store the total cost basis for all coins sold
total_cost_basis = 0

# Create a variable to store the total proceeds for all coins sold
total_proceeds = 0

# Loop through each sale transaction
for transaction in sales:
    
    # Calculate the cost basis for this sale 
    cost_basis = transaction['number_of_coins_sold'] * transaction['cost_per_coin_at_purchase']
    
    # Add the cost basis to the total cost basis
    total_cost_basis += cost_basis
    
    # Calculate the proceeds for this sale
    proceeds = transaction['number_of_coins_sold'] * transaction['selling_price_per_coin']
    
    # Add the proceeds to the total proceeds
    total_proceeds += proceeds
    
# Calculate the short term sales by subtracting the total cost basis from the total proceeds
short_term_sales = total_proceeds - total_cost_basis

# The short term sales will be commited and later we will be added the tax rates
print(short_term_sales)

# The Short term sales tax liability will be vary so it has mode detail to calculate exact tax figure
print(short_term_sales*15/100)
