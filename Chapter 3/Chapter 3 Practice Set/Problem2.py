# Write a program to fill in a letter template given below with name and date.
""" letter = Dear </Name/>
                      You are Selected!
                  </Date/>"""


letter = '''Dear <|Name|>,
You are Selected,
<|Date|>'''
print(letter.replace("<|Name|>", "Manish").replace("<|Date|>", "29 March 2025"))
  