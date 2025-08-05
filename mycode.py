# Input two odd numbers
num1 = int(input("Enter the first odd number: "))
num2 = int(input("Enter the second odd number: "))

# Check if both numbers are odd
if num1 % 2 != 0 and num2 % 2 != 0:
    # Calculate the sum
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
else:
    print("Both numbers must be odd. Please try again.")

