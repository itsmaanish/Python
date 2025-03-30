                                 # String Functions

# Find length of a String
word = "Hello World"
print(len(word))    #it counts from 1 to n

# String endswith()
name = "Manish"
print(name.endswith("sh"))  #True

# String Startswith()
name = "Samar"
print(name.startswith("s"))  #False  {bcz it is a case-sensitive}

# Count the String
name = "Samar Raj"
print(name.count("a"))   #It helps to count the total "No of Occurance"

# Capitalize
name = "samar"
print(name.capitalize())  #Samar

# Find Word
name = "Samar Raj"
print(name.find("a")) #1  --> returns idx of 1st occurance

# Replace
name = "Samar"
print(name.replace("Samar", "Manish"))