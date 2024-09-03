# Sample Python code to test VS Code setup

# Function to greet the user
def greet(name):
    return f"Hello, {name}! Welcome to your Python setup in VS Code."

# Main function
if __name__ == "__main__":
    # Ask for user's name
    user_name = input("Enter your name: ")
    
    # Call the greet function and print the result
    greeting = greet(user_name)
    print(greeting)

    # Basic arithmetic operation
    a = 5
    b = 3
    print(f"\nHere’s a basic arithmetic test:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
