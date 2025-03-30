# Write a Python program to detect the double spaces in a string

str = "Hello World  !"
if "  " in str:
  print("Double space is Detected!!")
else:
  print("No Double space found!!")

# 2nd way

str = "Hey There  !"
print(str.find("  "))  # it return 1st occurance idx value