"""
Find cube root
"""

# using while-loops
x = 8
ans = 0

while ans**3 < x:
    ans = ans + 1

if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# using for-loops
cube = 20
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break

if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
