print("Welcome to python pizza deliveries!")
print("This program will help you calculate the total cost of your pizza order.")
print("Please enter the size of the pizza you would like to order:")
print("S - Small")
print("M - Medium")
print("L - Large")
pizza_size = input("Enter the size of the pizza (S, M, L): ").strip().upper()
print("Please enter the type of pizza you would like to order:")
print("P - Pepperoni")
print("M - Margherita")
print("V - Vegetarian")
pizza_type = input("Enter the type of pizza (P, M, V): ").strip().upper()

print("Please enter the number of pizzas you would like to order:")
number_of_pizzas = int(input("Enter the number of pizzas: "))
print("Please enter the type of crust you would like:")
print("T - Thin")
print("D - Deep")
crust_type = input("Enter the type of crust (T, D): ").strip().upper()
print("Please enter the type of cheese you would like:")
print("R - Regular")
print("E - Extra")
cheese_type = input("Enter the type of cheese (R, E): ").strip().upper()

print("Please enter the type of sauce you would like:")
print("T - Tomato")
print("G - Garlic")

sauce_type = input("Enter the type of sauce (T, G): ").strip().upper()
print("Please enter the type of toppings you would like:")
print("O - Olives")
print("P - Peppers")
print("M - Mushrooms")
toppings_type = input("Enter the type of toppings (O, P, M): ").strip().upper()
print("Please enter the type of drink you would like:")
print("S - Soda")
print("W - Water")
drink_type = input("Enter the type of drink (S, W): ").strip().upper()
print("Please enter the type of dessert you would like:")
print("C - Cake")
print("I - Ice Cream")
dessert_type = input("Enter the type of dessert (C, I): ").strip().upper()
print("Please enter the type of delivery you would like:")
print("D - Delivery")
print("P - Pickup")
delivery_type = input("Enter the type of delivery (D, P): ").strip().upper()
print("Please enter the type of payment you would like:")
print("C - Cash")
print("C - Credit Card")
payment_type = input("Enter the type of payment (C, CC): ").strip().upper()
print("Please enter the type of discount you would like:")
print("S - Student")
print("M - Military")
discount_type = input("Enter the type of discount (S, M): ").strip().upper()

# Calculate the total cost of the pizza order
def calculate_total_cost(pizza_size, pizza_type, number_of_pizzas, crust_type, cheese_type, sauce_type, toppings_type, drink_type, dessert_type, delivery_type, payment_type, discount_type):
    # Base prices for different sizes
    size_prices = {
        'S': 8,
        'M': 10,
        'L': 12
    }
    
    # Base prices for different types of pizzas
    type_prices = {
        'P': 2,
        'M': 1,
        'V': 0
    }
    
    # Base prices for different types of crusts
    crust_prices = {
        'T': 1,
        'D': 2
    }
    
    # Base prices for different types of cheeses
    cheese_prices = {
        'R': 0,
        'E': 1
    }
    
    # Base prices for different types of sauces
    sauce_prices = {
        'T': 0,
        'G': 1
    }
    
    # Base prices for different types of toppings
    toppings_prices = {
        'O': 1,
        'P': 1,
        'M': 1
    }
    
    # Base prices for different types of drinks
    drink_prices = {
        'S': 2,
        'W': 1
    }
    # Base prices for different types of desserts
    dessert_prices = {
        'C': 3,
        'I': 2
    }
    # Base prices for different types of deliveries
    delivery_prices = {
        'D': 5,
        'P': 0
    }
    # Base prices for different types of payments
    payment_prices = {
        'C': 0,
        'CC': 1
    }
    # Base prices for different types of discounts
    discount_prices = {
        'S': 0.1,
        'M': 0.2
    }
    # Calculate the total cost
    total_cost = (size_prices[pizza_size] + type_prices[pizza_type] + crust_prices[crust_type] + cheese_prices[cheese_type] + sauce_prices[sauce_type] + toppings_prices[toppings_type] + drink_prices[drink_type] + dessert_prices[dessert_type] + delivery_prices[delivery_type] + payment_prices[payment_type]) * number_of_pizzas
    # Apply discount if applicable
    if discount_type in discount_prices:
        total_cost -= total_cost * discount_prices[discount_type]
    return total_cost
# Calculate the total cost of the pizza order
total_cost = calculate_total_cost(pizza_size, pizza_type, number_of_pizzas, crust_type, cheese_type, sauce_type, toppings_type, drink_type, dessert_type, delivery_type, payment_type, discount_type)
# Print the total cost of the pizza order
print(f"The total cost of your pizza order is: ${total_cost:.2f}")
# The code above is a simple program that calculates the total cost of a pizza order based on various options selected by the user.
# It takes into account the size, type, crust, cheese, sauce, toppings, drink, dessert, delivery method, payment method, and any applicable discounts.
# The program uses dictionaries to store the base prices for each option and calculates the total cost based on the user's selections.
# The program also applies any applicable discounts to the total cost.
# The final total cost is printed to the user in a formatted manner.

# The code above is a simple program that calculates the total cost of a pizza order based on various options selected by the user.
# It takes into account the size, type, crust, cheese, sauce, toppings, drink, dessert, delivery method, payment method, and any applicable discounts.
# The program uses dictionaries to store the base prices for each option and calculates the total cost based on the user's selections.
# The program also applies any applicable discounts to the total cost.      