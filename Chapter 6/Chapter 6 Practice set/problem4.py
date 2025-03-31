'''
Write a program which finds out whether a given name is present in a list or not
'''

names_list = ["Manish", "Raj", "Amit", "Suresh", "Priya", "Meghana"]


name = input("Enter the name to check: ")

# Checking if the name is in the list
if name in names_list:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is NOT present in the list.")

