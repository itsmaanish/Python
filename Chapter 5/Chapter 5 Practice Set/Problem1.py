''' Write a program to create a dictonary of Hindi words with values as their english Translator. Provide user with an option to look it Up! '''

dict = {
  "pustak" : "Book",
  "gaadi": "Vehical",
  "kutta" : "Dog",
  "kursi" : "Chair",
  "madad": "Help",
  "billi" : "Cat"
}

word = input("Enter Your word to translate it: ")
print(dict[word])
