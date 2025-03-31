''' Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use keys as their names. Assume that the names are unique '''

fav_language = {}

for i in range(4):
  name = input(f"Enter {i+1} name: ")
  language = input(f"Enter {name} language: ")
  fav_language[name] = language
print(fav_language)
