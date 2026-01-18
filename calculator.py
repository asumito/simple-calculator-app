import sys
from logic import collect_inputs, perform_calculation
# basically a prompt
initialize = input("What brings you here today? Simple calculations? (yes or no): ").lower()
if initialize != "yes":
    print("Goodbye")
    sys.exit()

print("--- Calculator Mode ---")

# Collects integers from user by using loop function in logic.py
user_numbers = collect_inputs()

# if user puts nothing, quit.
if not user_numbers:
    print("No numbers provided. Exiting.")
    sys.exit()

# Decide operation choice by user
operation = input("Choose an operation (add, subtraction, multiply, divide): ").lower()

# calculates
result = perform_calculation(user_numbers, operation)

# results [hopefully]
print(f"\nYour numbers: {user_numbers}")
print(f"The result of your {operation} is: {result}")
print("Calculation successful.")

sys.exit()