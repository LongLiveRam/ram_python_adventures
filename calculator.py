running = True
keepRunning = "y"

while running:
    result = num1 = num2 = 0
    operator = int(input("Please enter value\n"
                         "[1] Addition\n"
                         "[2] Subtraction\n"
                         "[3] Multiplication\n"
                         "[4] Division\n"
                         "[5] Close\n"))
    if operator is 5:
        running = False
        print("Thanks for using my calculator!")
    else:
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))

    if operator is 1:
        result = num1 + num2
    elif operator is 2:
        result = num1 - num2
    elif operator is 3:
        result = num1 * num2
    elif operator is 4:
        result = num1 / num2
    else:
        if running is not False:
            print(F"{operator} is not valid!")

    if running:
        print(F"The result is: {result}")
        keepRunning = input("Would you like to continue? y/n")
        if keepRunning is "n":
            print("Thanks for using my calculator!")
            running = False
