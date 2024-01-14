# Ground Shipping
weight = 41.5
ground_shipping_flat_charge = 20.00

cost = ""

if weight <= 2:
    cost = 1.50
elif 3 <= weight <= 6:
    cost = 3.00
elif 7 <= weight <= 10:
    cost = 4.00
else:
    cost = 4.75

ground_shipping = weight * cost + ground_shipping_flat_charge
ground_shipping_premium = 125.00

print(ground_shipping)
print(ground_shipping_premium)

# Drone Shipping

drone_shipping_flat_charge = 0

weight = 41.5
cost = ""

if weight <= 2:
    cost = 4.50
elif 3 <= weight <= 6:
    cost = 9.00
elif 7 <= weight <= 10:
    cost = 12.00
else:
    cost = 14.25

drone_shipping = weight * cost + drone_shipping_flat_charge
print(drone_shipping)

# For a 4.8 pound package
# ground_shipping would be the cheapest option
# at $34.40

# For a 4.8 pound package
# ground_shipping_premium would be the cheapest option
# at $34.40
