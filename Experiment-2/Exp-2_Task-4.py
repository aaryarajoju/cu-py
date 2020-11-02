# EXPERIMENT - 2
# TASK - 4 : Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500) against a given amount

def numOfNotes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
 
amount = int(input("Enter the amount: "))
print(numOfNotes(amount))
