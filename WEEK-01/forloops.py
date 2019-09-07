"""
a += b is equivalent to a = a + b
a -= b is equivalent to a = a - b
a *= b is equivalent to a = a * b
a /= b is equivalent to a = a / b
"""

num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

"""
"""
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

"""
"""
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

"""
"""

num = 10
while num > 3:
    num -= 1
    print(num)


num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')


num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))


"""
There are three ways you can call range():

range(stop) takes one argument.
range(start, stop) takes two arguments.
range(start, stop, stepsize) takes three arguments.

Incrementing with range() - positive step number
Decrementing with range() - negative step number

range(5) => range(0,5) => 0,1,2,3,4
"""


"""
Q1: Increment by 2
"""
for x in range(2, 12, 2):
    print(x)
print("Goodbye!")

n = 0
while n < 10:
    n += 2
    print(n)
print("Goodbye!")

"""
Q2: Decrement by 2 in reverse
"""
print("Hello!")
n = 10
while n > 0:
    print(n)
    n -= 2

# Reverse numbers in range by decrementing step size
print("Hello!")
for x in range(10, 0, -2):
    print(x)

"""
Q3: sum of numbers
"""
end = 6
start = 0
x = 0
while start < end:
    start += 1      # increment the counter
    x = x + start   # store the counter value and add to itself
    # print(start)
print(x)

end = 6
x = 0
for i in range(1, (end+1)):
    x = x + i

print(x)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

for letter in 'hola':
    print(letter)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    # break
print(count)


myStr = '6.00x'

for char in myStr:
    print(char)

print('done')


"""
print even letters
"""
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print('even ' + letter)
    print(letter)

print('done')

"""
Find vowels and consonants in a string
"""
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))


iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1


for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))


for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break


count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))


count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))


count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))


num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)


num = 10
while num > 3:
    num -= 1
    print(num)

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')


num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 


numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
