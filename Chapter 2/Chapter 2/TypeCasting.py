# Learn about the type() and typecasting

# 1. Converting to Integer (int())
# Float to Integer
num = int(10.9)  # decimal part remove ho jayega
print(num, type(num))

# String to Integer
name = int("50")
print(name, type(name))

# ---------------------------------------------------------------------
# 2. Converting to Float (float())
# Integer to Float
a = 20
f = float(a)
print(f, type(f))

# ---------------------------------------------------------------------
# 3. Converting to String (str())
# Integer to String
num = str(100)
print(num, type(num))

# ---------------------------------------------------------------------
# 4. Converting to Boolean (bool())
# Integer to Boolean

print(bool(0))
print(bool(1))
print(bool(100))

# ---------------------------------------------------------------------
# 5. Converting to List, Tuple, Set

# String to List
text = "Hello"
text_list = list(text)  # ['H', 'e', 'l', 'l', 'o']
print(text_list)

# List to Tuple
num_list = [1, 2, 3]
num_tuple = tuple(num_list)
print(num_tuple)

# List to Set
num_set = set(num_list)
print(num_set)


# String to Tuple
name = "Manish"
str_tuple = tuple(name)
print(str_tuple, type(str_tuple))