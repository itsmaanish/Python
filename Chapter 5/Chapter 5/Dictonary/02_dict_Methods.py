dict = {
  "name" : "Manish",
  "Marks" : 87,
  "Subject": "Computer",
  0 : "Samar",
  "list" : [1,2,3]
}

print(dict.items())
print(dict.keys())
print(dict.values())

dict.update({"Marks" : 99})   #Case-sensitive
print(dict)

print(dict.get("name"))

