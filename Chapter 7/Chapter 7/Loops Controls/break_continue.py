for i in range(20):
  if(i==20):
    break  # terminate the loop immediately
  print(i)

print("---------------------------------------")

for i in range(10): # skip the current iteration and continue with the next one
  if i == 5:
    continue
  print(i)