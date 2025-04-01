'''
Write a multiplication table in reverse
'''

num = int(input("Enter the number: "))

for i in range(10, 0, -1):
  print(f"The table of {num}x{i}  is: ", num * i)