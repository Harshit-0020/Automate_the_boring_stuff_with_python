import pyinputplus as pi
import time

bread_prices = {
                    'White': 50,
                    'Wheat': 40,
                    'Sourdough': 60
}

protein_prices = {
                    'Chicken': 50,
                    'Turkey': 60,
                    'Ham': 50,
                    'Tofu': 30
}

cheese_prices = {
                    'Cheddar': 50,
                    'Swiss': 60,
                    'Mozzarella': 50
}

toppings_prices = {
                    'Mayo': 20,
                    'Mustard': 10,
                    'Lettuce': 15,
                    'Tomato': 10,
}

total = 0

bread_type = pi.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
print(f"Bread selected: {bread_type}")
total += bread_prices[bread_type]
time.sleep(1)

protein_type = pi.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
print(f"Protein selected: {protein_type}")
total += protein_prices[protein_type]
time.sleep(1)

want_cheese = pi.inputYesNo(prompt='Would you like cheese in your Sandwich? (Yes/No) ')
if want_cheese == 'yes':
    cheese_type = pi.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'],
                               prompt='Which cheese would you like? \n', numbered=True)
    print(f"Cheese selected: {cheese_type}")
    total += cheese_prices[cheese_type]
else:
    print("No cheese selected")
time.sleep(1)

toppings = ['Mayo', 'Mustard', 'Lettuce', 'Tomato']
for i in range(len(toppings)):
    answer = pi.inputYesNo(prompt=f"Do you want {toppings[i]}?")
    if answer == 'yes':
        print(f"{toppings[i]} added.")
        total += toppings_prices[toppings[i]]
        time.sleep(1)

no_of_sandwiches = pi.inputInt(prompt="How many sandwiches do you want? ")
print(f"Making {no_of_sandwiches} sandwiches.")
total = total * no_of_sandwiches
time.sleep(1)
print(f"Your total price is: {total}.\nPlease visit again.\nHave a nice day!")
time.sleep(1)
