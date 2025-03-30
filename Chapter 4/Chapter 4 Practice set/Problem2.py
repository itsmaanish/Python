# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
  mark = int(input(f"Enter the Student marks {i+1} "))  #String --> int
  marks.append(mark)

print("Before Marks Sorted: \n", marks)
print("----------------------------------")
marks.sort()
print("After Marks Sorted: \n", marks)




