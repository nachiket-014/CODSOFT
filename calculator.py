# python programming internship in codsoft 
# task  -- calculator

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")
    choices = ['1', '2', '3', '4']

    if choice == '5':
        print("Exiting the calculator")
        break

    if choice in choices:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        num1 = float(num1)
        num2 = float(num2)

        if choice == '1':
            result = num1 + num2
            print(num1 ,'+' , num2 ,'=' ,result)

        elif choice == '2':
            result = num1 - num2
            print(num1 ,'-' , num2 ,'=' ,result)

        elif choice == '3':
            result = num1 * num2
            print(num1 ,'*' , num2 ,'=' ,result)

        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print(num1 ,'/' , num2 ,'=' ,result)
    else:
        print("Invalid input! Please enter a number between 1 and 5.")
