# EXPERIMENT - 2
# TASK - 2 : Write a Python function to find the Max of three numbers

def maximum(x,y,z):
    return max(x,y,z)

#main
x, y, z = input("Enter a three value: ").split()
print(maximum(x,y,z))
