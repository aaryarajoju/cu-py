# EXPERIMENT - 2
# TASK - 5 : Create a program wages.py that assumes people are paid double time for hours over 60. They get paid for at most 20 hours overtime at 1.5 times the normal rate.

#wages.py

import random

def printSalary(hours, wage):
    if hours < 40:
        print("The salary cannot be generated")
        print('\a')
    elif hours >= 40 :
        print(salary(hours, wage))

def salary(hours, wage):
    if hours == 40:
        OTsalary = 40 * wage
    elif hours > 40 and hours < 60:
        OTsalary = 40 * wage + (hours-40)*(1.5*wage)
    elif hours > 60:
        OTsalary = 40 * wage + 20*(1.5*wage) + (hours-60)*(2*wage)
    return OTsalary

#main
numOfHours  = random.randint(35,75)
regularWage = int(input("Enter the regular wage: "))
print("The number of hours are:", numOfHours)
printSalary(numOfHours, regularWage)
