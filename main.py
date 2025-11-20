def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers, handling divide by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def print_menu():
    """Print the calculator menu options."""
    print("\n=== Simple Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    """Main function to run the calculator program."""
    while True:
        print_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting... Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operation = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"
        elif choice == "4":
            result = divide(num1, num2)
            operation = "/"

        if isinstance(result, (int, float)):
            print(f"Result: {num1} {operation} {num2} = {round(result, 2)}")
        else:
            print(result)

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break


# ✅ VERY IMPORTANT: This line actually RUNS the program
if __name__ == "__main__":
    main()
