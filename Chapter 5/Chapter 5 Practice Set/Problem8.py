'''Can you change the value inside the list which is contained in a Set s '
  s = {8, 7, 12, "Manish", [1,2]} 
Answer --> No
'''

s = {8, 7, 12, "Manish", [1,2]}
print(s)   # Error

'''
❌ No, you cannot create a set s with a list inside it because lists are mutable (changeable), and sets only allow immutable (unchangeable) elements.

----------------------------------------------------
📌 Why?
In Python, sets only store immutable (unchangeable) objects, and lists are mutable (their elements can be modified).

Thus, the following code will raise a TypeError:

python

s = {8, 7, 12, "Manish", [1, 2]}  # ❌ This will cause an error
🔹 Error Message:
TypeError: unhashable type: 'list'

----------------------------------------------------------------------------
✅ Correct Alternative
If you want to store multiple values inside a set, use a tuple instead of a list, because tuples are immutable:

s = {8, 7, 12, "Manish", (1, 2)}  # ✅ This works!
print(s)

🔹 Output
{8, 7, 12, 'Manish', (1, 2)}

'''