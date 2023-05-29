from datetime import datetime

def calculate_long_term_capital_gain(purchase_price, sale_price, purchase_date, sale_date):
    if not purchase_date or not purchase_price:
        return sale_price  # Consider as full profit if purchase details are missing
    
    purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
    sale_date = datetime.strptime(sale_date, '%Y-%m-%d')
    holding_period = (sale_date - purchase_date).days

    if holding_period <= 365:
        return 0

    capital_gain = sale_price - purchase_price
    return capital_gain


# Sample data needed with purchase date and sale date
transactions = [
    {"purchase_price": 1000, "sale_price": 2000, "purchase_date": "2022-01-01", "sale_date": "2023-01-02"},
    {"purchase_price": None, "sale_price": 1500, "purchase_date": None, "sale_date": "2023-06-03"},
    {"purchase_price": 1000, "sale_price": 3000, "purchase_date": "2021-12-01", "sale_date": "2023-12-01"},
    # Add more transactions here
]

total_income = 0

for transaction in transactions:
    income = calculate_long_term_capital_gain(
        transaction["purchase_price"],
        transaction["sale_price"],
        transaction["purchase_date"],
        transaction["sale_date"]
    )
    total_income += income

print("Total long-term capital gain income:", total_income)
