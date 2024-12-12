def divide_numbers():
    try:
        number = input("Enter a number: ")
        divisor = input("Enter the divisor: ")

        number = float(number)
        divisor = float(divisor)

        result = number / divisor
        print(f"The result of {number} divided by {divisor} is: {result}")

    except ValueError:

        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:

        print("Error: Division by zero is not allowed.")



divide_numbers()
