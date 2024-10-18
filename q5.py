def sum_of_digits():
    # Get user input
    number = input("Enter an integer: ")
    
    # Initialize sum variable
    total = 0
    
    # Loop through each character in the string representation of the number
    for digit in number:
        # Ensure we only process digits
        if digit.isdigit():
            total += int(digit)
    
    return total

if __name__ == '__main__':
    result = sum_of_digits()
    print("The sum of the digits is:", result)

