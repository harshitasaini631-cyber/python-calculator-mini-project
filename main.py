def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

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

        print(f"Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
