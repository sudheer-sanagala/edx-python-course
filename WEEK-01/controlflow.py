"""
    Write a piece of Python code that prints out the string 'hello world' if the value of an integer variable, happy, is strictly greater than 2.
"""

happy = 5

if happy > 2:
    print("hello world")
else:
    print("")


"""
Assume that two variables, varA and varB, are assigned values, either numbers or strings. Write a piece of Python code that evaluates varA and varB,
 and then prints out one of the following messages
"""
varA = "Sudheer"
varB = "Sanagala"

if (type(varA) == str or type(varB) == str):
    print("strings involved")

    if (len(varA) > len(varB)):
        print("bigger")
    elif (len(varA) == len(varB)):
        print("equal")
    elif (len(varA) < len(varB)):
        print("smaller")
else:
    if (varA > varB):
        print("bigger")
    elif (varA == varB):
        print("equal")
    elif (varA < varB):
        print("smaller")
