"""A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
 the percent tip they want to leave. Then print both the tip amount and the total bill with the
 tip included."""

meal_price = eval(input("Enter your meal price: #"))
percent_tip = eval(input("What percent price tip do you want to leave?: "))
percent_tip_converted = percent_tip / 100
tip_amount = meal_price * percent_tip_converted
total_bill = meal_price + tip_amount
print(f"The tip amount on your meal price is {tip_amount}\nThe total bill including the tip amount is {total_bill}")