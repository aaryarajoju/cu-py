# EXPERIMENT - 2
# TASK - 3 : Write a Python function that takes a list and returns a new list with unique elements of the first list.

def uniqueList(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(uniqueList([1,2,3,3,3,3,4,5,5,5])) 
