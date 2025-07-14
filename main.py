
import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return "Error: Cannot divide by zero" if y == 0 else x / y
def power(x, y):
    return x ** y
def modulo(x, y):
    return x % y
def square_root(x):
    return math.sqrt(x)

def calculator():
    while True:
        print("\n--- Advanced Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Modulo (x % y)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Thanks for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '7']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Enter numeric values.")
                continue

            if choice == '1':
                print("Result:", add(x, y))
            elif choice == '2':
                print("Result:", subtract(x, y))
            elif choice == '3':
                print("Result:", multiply(x, y))
            elif choice == '4':
                print("Result:", divide(x, y))
            elif choice == '5':
                print("Result:", power(x, y))
            elif choice == '7':
                print("Result:", modulo(x, y))

        elif choice == '6':
            try:
                x = float(input("Enter number: "))
                if x < 0:
                    print("Error: Cannot compute square root of negative number.")
                else:
                    print("Result:", square_root(x))
            except ValueError:
                print("Invalid input. Enter a number.")

        else:
            print("Invalid choice. Try again.")

# Run it
calculator()


