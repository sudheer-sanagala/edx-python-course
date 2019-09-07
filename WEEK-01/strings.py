hi = "Hello Sudheer"
print(hi)

hi = 'Hello Sudheer'
print(hi)

# concatenate string
greet = hi + "World"
print(greet)  # Hello SudheerWorld

greet = hi + " " + "World"
print(greet)  # Hello Sudheer World

# multiply string
print(3*'sudheer')  # sudheersudheersudheer

print('world'*3)  # worldworldworld

print('3'*'sudheer')  # ERROR - can't multiply sequence by non-int of type 'str'

# extract elements of string
# u - string starts with 0. In this case `u` is the element at position 1
print('sudheer'[1])

print('sudheer'[-1])  # r --prints a character at the index[1] from reverse

print('sudheer'[-2])  # e --prints a reverse of string

name = 'sudheer'
print(name[1])  # u


# slicing strings
print('sudheer'[1:3])  # ud -- prints elements from index[1] till index[3]

print('sudheer'[:3])  # sud -- all elements upto position 3 i.e 0,1,2

print('sudheer'[1:])  # udheer -- all elements starting from position 1

print('sudheer'[:-1])  # sudhee -- rever a string from index[1]

print('sudheer'[:])  # sudheer -- copies the exact string

# slicing string with step-size
print('sudheer'[0:7:2])  # sder

# sder -- prints from index[0] till end, but increments of 2
print('sudheer'[::2])

# shr -- prints from index[0] till end, but increments of 3
print('sudheer'[::3])

# uhe -- prints from index[0] till end, but increments of 3
print('sudheer'[1::2])

print('helloworld'[1:9:2])  # elwr

print('helloworld'[::-1])  # dlrowolleh -- REVERSE A STRING


#
str1 = 'hello'
str2 = ','
str3 = 'world'

# print(str1[len(str1)]) # len[str1] is 5 and the string index is from 0..4

print(str1 + str2 + str3)

print('world'*3)
