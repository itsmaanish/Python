'''
Write a program to find greatest of four numbers entered by the users.
'''

n1 = int(input(f"Enter the 1st number is: "))
n2 = int(input(f"Enter the 2nd number is: "))
n3 = int(input(f"Enter the 3rd number is: "))
n4 = int(input(f"Enter the 4th number is: "))

if(n1>n2):
  print("n1 is greater ", n1)
elif(n2>n3):
  print("n2 is greater ", n2)
elif(n3>n4):
  print("n3 is greater ", n3)
else:
  print("n4 is greater ", n4)

