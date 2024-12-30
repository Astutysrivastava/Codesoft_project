def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        choice = int(input("Enter the number corresponding to your choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please choose a valid operation.")
            return
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            result = add(num1, num2)
            operation = "+"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "-"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "*"
        elif choice == 4:
            result = divide(num1, num2)
            operation = "/"
        
        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error! Invalid input. Please enter numbers only.")

# Run the calculator
if __name__ == "__main__":
    calculator()
