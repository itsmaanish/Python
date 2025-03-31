#  Write a program to input 8 numbers from the user and display all the Unique Numbers

num = set()

for i in range(8):
  number = int(input(f"Enter {i+1} number: "))
  num.add(number)
print(num)