  # EXPERIMENT - 2
# TASK - 5 : Create a program wages.py that assumes people are paid double time for hours over 60. They get paid for at most 20 hours overtime at 1.5 times the normal rate.

#wages.py

import random

numOfHours  = random.randint(35,75)
regularWage = int(input("Enter the regular wage: "))
print("The number of hours are:", numOfHours)

if numOfHours < 40:
  print("The salary cannot be generated")
  print('\a')
elif numOfHours == 40:
  print(40 * regularWage)
elif numOfHours > 40 and numOfHours < 60:
  print(40 * regularWage + (numOfHours-40)*(1.5*regularWage))
else:
  print(40 * regularWage + 20*(1.5*regularWage) + (numOfHours-60)*(2*regularWage))
