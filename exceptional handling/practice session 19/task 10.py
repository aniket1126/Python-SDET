def divide_numbers():
    try:
        number = float(input("Enter a number: "))
        divisor = float(input("Enter the divisor: "))

        result = number / divisor
        print(f"The result of {number} divided by {divisor} is: {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    finally:
        print("Execution completed, exiting program.")

divide_numbers()
