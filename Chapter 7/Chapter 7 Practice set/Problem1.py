'''
Write a program to print multiplication table of a given number using FOR LOOP
'''

num = int(input("Enter the number: "))

for i in range(1, 10):
  print(f"The table of {num}x{i}  is: ", num * i)
