"""
Square of a given number 
ex: 3^2 = 3*3 = 9; 5^2 = 5*5 = 25 
"""
# using while-loop
x = 4
ans = 0
itersLeft = x     # no of iterations remaining

while(itersLeft != 0):  # while no of iterations not equal to 0
    ans = ans + x  # add the same number by itself for thje total no of loops
    itersLeft = itersLeft - 1  # reduce the iteration loop by 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

# using for-loop
x = 4
ans = 0

for i in range(x):
    ans = ans + x
print(str(x) + '*' + str(x) + ' = ' + str(ans))
