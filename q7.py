def calculate_factorial(n):
    # Initialize the result to 1 (factorial of 0 and 1 is 1)
    factorial = 1
    
   
    for i in range(1, n + 1):
        factorial *= i  # Multiply each integer to the result
    
    return factorial


if __name__ == '__main__':
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Please enter a positive integer.")
    else:
        result = calculate_factorial(number)
        print(f"The factorial of {number} is: {result}")
