# System function to quit the script if no.
import sys
# A simple calculator app built with python, run using CLI.
question_to_user = input("What brings you hear today? Simple calculations? (yes or no)" )
if question_to_user=="yes": 
    print("Calculator")
else:
    print("Goodbye")
    sys.exit()

# Different Variables for 10 inputs
p = int(input("What would your first number be  "))
q = int(input("What would your second number be  "))
r = int(input("What would your third number be  "))
s = int(input("What would your fourth number be  "))
u = int(input("What would your sixth number be  "))
v = int(input("What would your seventh number be  "))
w = int(input("What would your eighth number be  "))
x = int(input("What would your nineth number be  "))
y = int(input("What would your tenth number be  "))

# Handles what to do with the inputs above
operation = input("Choose an operation (add, subtraction, multiply, divide): ").lower()
if operation=="add":
    result = p + q + r + s + u + v+ w +x +y
    print(f"The total sum is {result}")

elif operation == "subtraction":
    result = p - q - r - s - u - v - w - x - y
    print(f"The differnce is {result}")

elif operation == "multiply":
    result = p * q * r * s * u * v * w * x * y
    print(f"The product is {result}")

elif operation == "divide":
    result = p / q / r / s / u / v / w / x / y
    print(f"The quotient is {result}")

else:
    print("Invalid operation selected.")


print("Calculation result is successful and stated above.")
sys.exit()
