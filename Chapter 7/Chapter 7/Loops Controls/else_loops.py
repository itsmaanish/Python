'''
Python allows using else with both for and while loops. The else block executes only if the loop finishes normally (without break).
'''
# For Loop with else
for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully.")

# while loop with else
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed.")
