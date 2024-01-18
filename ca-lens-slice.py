# Len's Slice

# Task 1, 2
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Task 3, 4 ,5
num_two_dollar_slices = prices.count(2)
print("Number of $2 slices: " + str(num_two_dollar_slices))
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizzas")

# Task 6, 7
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"],
                    [2, "mushrooms"]]
print("List of pizzas and prices: " + str(pizza_and_prices))

# Task 8
pizza_and_prices.sort()
# check
# print(pizza_and_prices)

# Task 9
cheapest_pizza = pizza_and_prices[0]
# check
# print(cheapest_pizza)

# Task 10
priciest_pizza = pizza_and_prices[-1]
# check
# print(priciest_pizza)

# Task 11, 12
pizza_and_prices.remove([7, "anchovies"])
# check
# print(pizza_and_prices)

pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print("Anchovies sold out! Here's an updated menu: " + str(pizza_and_prices))

# Task 13
three_cheapest = pizza_and_prices[:3]
print("Here are the cheapest 3 pizzas for those kind mice: " + str(three_cheapest))
