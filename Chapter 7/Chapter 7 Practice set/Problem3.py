# solve the Problem 1 with using While loop
'''
Write a program to print multiplication table of a given number using While LOOP
'''

num = int(input("Enter the value: "))
i = 1

while(i<=10):
  print(f"{num}x{i} = ", num*i)
  i+=1