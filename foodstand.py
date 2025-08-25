foods = {"fishball": 2.00, "kikiam": 2.50, "squidball": 3.00,
         "kwekkwek": 12.00, "tokneneng": 10.00, "isaw": 8.00}
cart = []
total = 0
ordering = True
while ordering:
    print("------- Menu Items -------")
    for key, value in foods.items():
        print(f"{key:10} : ₱{value:.2f}")
    food = input("Please enter your food or (q to quit): ").lower()
    if food.lower() == "q":
        print("Thanks for your patronage!")
        ordering = False
    elif foods.get(food) is not None:
        print(f"{food.capitalize()} added to cart!")
        cart.append(food)
print("Here's your cart: ")
for food in cart:
    print(f"{food.capitalize():.<25}{foods.get(food)}")
    total += foods.get(food)
print(f"Your total is {total:.2f} pesos!")
