'''
Write a program to find out whether a student is  pass or fail, if it requires total 40% and at least 33%, in each subject to pass. Assuem 3 subject and take marks as an input from the user.
'''

marks1 = int(input("Enter the 1st Subject marks: "))
marks2 = int(input("Enter the 2nd Subject marks: "))
marks3 = int(input("Enter the 3rd Subject marks: "))

marks_obtained = (marks1+marks2+marks3)/300
perc = (marks_obtained)*100

if(perc>=40 and marks1>33 and marks2>33 and marks3>33):
  print("Pass")
else:
  print("Fail")