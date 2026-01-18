def collect_inputs():
    """Loops to collect an unknown amount of numbers from the user."""
    numbers = []
    print("Enter your numbers one by one. Type 'done' when you are finished.")
    
    while True:
        data = input("Enter number: ")
        
        if data.lower() == 'done':
            break
            
        try:
            # float to calculate decimals
            num = float(data)
            numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a number or type 'done'.")
            
    return numbers

def perform_calculation(numbers_list, operation):
    """Takes a list and a string, then performs the requested math."""
    
    if operation == "add":
        return sum(numbers_list)

    elif operation == "multiply":
        result = 1
        for n in numbers_list:
            result = result * n
        return result

    elif operation == "subtraction":
        # start with largest number
        result = numbers_list[0]
     
        for n in numbers_list[1:]:
            result = result - n
        return result

    elif operation == "divide":
        result = numbers_list[0]
        for n in numbers_list[1:]:
            if n == 0:
                return "Error: Division by zero"
            result = result / n
        return result

    else:
        return "Unknown Operation"