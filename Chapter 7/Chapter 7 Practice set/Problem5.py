'''
Write a program to find the sum of 1st n natural nummbers using while loop
'''

num = int(input("Enter the number "))
i = 1
sum = 0

while(i<=num):
  sum = sum+i
  print(sum)
  i+=1