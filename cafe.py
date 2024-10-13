
menu = ["Moca", "Tea", "Cheese_Cake", "Wrap"] # A list containing the cafe's menu items.
stock = {"Moca": 15, "Tea": 12, "Cheese_Cake": 8, "Wrap": 20} # A dictionary with menu items as keys and their corresponding stock quantities as values.
price = {"Moca": 5.50, "Tea": 1.30, "Cheese_Cake": 7.00, "Wrap": 2.00} # A dictionary with menu items as keys and their corresponding prices as values.

total_stock_worth = 0
for item in menu: # Access stock quantity and price using item as the key in dictionaries
  item_quantity = stock[item]
  item_price = price[item]

  item_value = item_quantity * item_price # Calculate the total value of each item (stock * price)

  total_stock_worth += item_value # Add the value of each item to the total stock worth

print(f"The total stock value in the cafe is: £{total_stock_worth:.2f}") # Print the total stock value with two decimal places

