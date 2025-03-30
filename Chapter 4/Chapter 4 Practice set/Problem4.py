# Write a program to sum a list with 4 numbers

numbers = []

for i in range(3):
  num = int(input(f"Enter Your Number {i+1}: "))
  numbers.append(num)

print(sum(numbers))