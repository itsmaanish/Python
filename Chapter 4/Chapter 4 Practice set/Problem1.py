# Write a Python program to store seven fruits in a list entered by the user.

fruits = []

for i in range(7):
  fruit = input(f"Enter fruit {i+1: } ")
  fruits.append(fruit)

print(fruits)
