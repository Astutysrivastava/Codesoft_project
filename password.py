import random
import string

def generate_password(length, complexity):
    """
    Generate a password based on the specified length and complexity.

    Parameters:
        length (int): The length of the password.
        complexity (int): The complexity level of the password (1-3).

    Returns:
        str: A generated password.
    """
    if complexity == 1:  # Only lowercase letters
        characters = string.ascii_lowercase
    elif complexity == 2:  # Lowercase, uppercase, and digits
        characters = string.ascii_letters + string.digits
    elif complexity == 3:  # Lowercase, uppercase, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose between 1 and 3.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        print("Select the complexity level:")
        print("1. Low (only lowercase letters)")
        print("2. Medium (lowercase, uppercase, and digits)")
        print("3. High (lowercase, uppercase, digits, and special characters)")
        
        complexity = int(input("Enter the complexity level (1/2/3): "))
        if complexity not in [1, 2, 3]:
            print("Invalid complexity level. Please choose between 1 and 3.")
            return

        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the application
if __name__ == "__main__":
    main()
