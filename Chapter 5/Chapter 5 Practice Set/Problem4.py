''' What will be the length of following set s
s = set()
s.add(20)
s.add(20.0)

'''

s = set()
s.add(20)
s.add(20.0)

print(s)
print(len(s))

# ✅ Explanation:
# 20 (int) and 20.0 (float) are considered the same in a set because 20 == 20.0 evaluates to True in Python.

# Sets store only unique values, so even though both 20 (integer) and 20.0 (float) are added, they are treated as a single element.

# Hence, len(s) = 1.