
import matplotlib

import matplotlib.pyplot as plt


#Function to calculate the number of smartphones to order based on price and stock levels

def calculate_tobuy(last_price, average_price, instock):
    if last_price < 0.7 * average_price and instock < 30: #if the price has dropped significantly and stock is low
        return 15 # Order 15 units
    elif instock < 10: #if the stock level is critically low
        return 5 # Order 5 units
    else: #if stock levels are sufficient
        return 0 # No need to order

#Implementing the trading agent
def trading_agent(price_history, stock_levels, average_price):
    tobuy_history = []
    for price, instock in zip(price_history, stock_levels):
        # If the price is significantly lower than the average price (e.g., 20% discount), consider ordering more
        if price < 0.8 * average_price:  # 20% discount from average price
            if instock < 10:  # Critically low stock
                tobuy = 10
            else:  # Stock level not critically low
                tobuy = 15
        else:
            tobuy = calculate_tobuy(price, average_price, instock)  # Use the custom logic to decide the order quantity
        tobuy_history.append(tobuy)
    return tobuy_history

# Example data
price_history = [600, 500, 550, 450, 400, 650]  # Current prices over time
stock_levels = [20, 15, 5, 25, 8, 12]            # Stock levels over time
average_price = 600                              # Average price of the smartphone

# Apply the trading agent

tobuy_history = trading_agent(price_history, stock_levels, average_price)

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(price_history, label='Price')
plt.plot(stock_levels, label='Stock Levels')
plt.plot(tobuy_history, label='ToBuy', linestyle='--', marker='o')
plt.axhline(0.8 * average_price, color='red', linestyle='--', label='20% Discount Threshold')
plt.xlabel('Time (Index)')  # X-axis label
plt.ylabel('Values')        # Y-axis label
plt.title('Trading Agent Decision Over Time')  # Title of the plot
plt.legend()  # Show the legend to identify each line
plt.grid()    # Add a grid to the plot
plt.show()    # Display the plot
