  
# EXPERIMENT - 2
# TASK - 5 : Create a program wages.py that assumes people are paid double time for hours over 60. They get paid for at most 20 hours overtime at 1.5 times the normal rate.

#wages.py

import random

numOfHours  = random.randint(35,75)
regularWage = int(input("Enter the regular wage: "))

if hours < 40:
  print("The salary cannot be generated")
  print('\a')
elif hours == 40:
  print(40 * wage)
elif hours > 40 and hours < 60:
  print(40 * wage + (hours-40)*(1.5*wage))
else:
  print(40 * wage + 20*(1.5*wage) + (hours-60)*(2*wage))

print("The number of hours are:", numOfHours)
printSalary(numOfHours, regularWage)
