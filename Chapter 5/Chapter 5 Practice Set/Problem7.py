''' If names of 2 friends are the same; What will happen to the program in Program 6'''

fav_language = {}

for i in range(4):
  name = input(f"Enter {i+1} name: ")
  language = input(f"Enter {name} language: ")
  fav_language[name] = language
print(fav_language)


'''
Enter 1 name: Aman
Enter Aman language: Python

Enter 2 name: Rahul
Enter Rahul language: Java

Enter 3 name: Aman
Enter Aman language: C++

Enter 4 name: Neha
Enter Neha language: JavaScript

# Output-------------------------------------------------
{'Aman': 'C++', 'Rahul': 'Java', 'Neha': 'JavaScript'}
# Output-------------------------------------------------


'''

'''
✅ Explanation
The first entry for "Aman" is stored as {'Aman': 'Python'}.

When "Aman" is entered again, its previous value is overwritten, and it becomes {'Aman': 'C++'}.

The dictionary does not allow duplicate keys, so only the latest entry remains.
'''