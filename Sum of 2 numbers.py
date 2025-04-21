num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
  sum_of_numbers = int(num1) + int(num2)
  print("The sum is:", sum_of_numbers)
except ValueError:
  print("Invalid input. Please enter numbers only.")
