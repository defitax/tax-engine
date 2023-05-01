#create a purchase history for similar transcations only related to purchases
Purchases = [
    {'cost_per_coin_at_purchase': cost_per_coin, 'number_of_coins_purchase': num_purchase}
]


#There will be few lists will be added to understand the difference between to two users transactions. This was only the complete of one layer there will be more added and connected with all time line accross the core areas.
num_sold = input("Give me the number of coins sold\n")
cost_per_coin = input("How much the coin price at the time of purchase\n")
selling_per_coin = input("At what price you sold the coin\n")
num_purchase 


# Define the list of sale transactions as a list of dictionaries
sales = [
    {'number_of_coins_sold': num_sold, 'cost_per_coin_at_purchase': cost_per_coin, 'selling_price_per_coin': selling_per_coin}
]

# Create a variable to store the total cost basis for all coins sold
total_cost_basis = 0

# Create a variable to store the total proceeds for all coins sold
total_proceeds = 0
# Create a purchase data over last transcations 
purchase = input("create from api")

# Loop through each sale transaction
for transaction in sales:
    
    # Calculate the cost basis for this sale
    cost_basis = transaction[num_sold] * transaction[cost_per_coin]
    
    # Add the cost basis to the total cost basis
    total_cost_basis += cost_basis
    
    # Calculate the proceeds for this sale
    proceeds = transaction[num_sold] * transaction[selling_per_coin]
    
    # Add the proceeds to the total proceeds
    total_proceeds += proceeds
    
# Calculate the short term sales by subtracting the total cost basis from the total proceeds
short_term_sales = total_proceeds - total_cost_basis

# The short term sales will be commited and later we will be added the tax rates
print(short_term_sales)


