def add(a, b):
    """Return the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b

def multiply(a, b):
    """Return the product of two numbers"""
    return a * b

def divide(a, b):
    """Retyrn the divison of two numbers """
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
    while True:
        #display menu options
        print_menu()

        #take user choice
        choice = input("Enter your choice (1-5): ")

        #exit condition
        if choice == "5":
            print("Exiting... Goodbye!")
            break
        
          # Validate choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue
        
        # Take number inputs
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        
         # Perform selected operation
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
      
        # Display result  
        if isinstance(result, (int, float)):
            print(f"Result: {num1} {operation} {num2} = {round(result, 2)}")
        else:
            print(result)

        
        # Ask user if they want to continue
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break
