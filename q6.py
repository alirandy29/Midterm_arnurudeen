def reverse_string(input_string):

    reversed_string = ""
    
   
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    
    return reversed_string


if __name__ == '__main__':
    user_input = input("Enter a string: ")
    result = reverse_string(user_input)
    print("Reversed string:", result)
