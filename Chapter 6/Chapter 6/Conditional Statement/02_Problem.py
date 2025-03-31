'''
Write a Python program to take the age value from the user and check if his age is greater than 18 then He can Vote otherwise Not
'''

age = int(input("Enter Your Age: "))
print(age)

if(age >= 18):
  print("Eligibal for Vote!")
else:
  print("Not Eligibal for Vote!!")