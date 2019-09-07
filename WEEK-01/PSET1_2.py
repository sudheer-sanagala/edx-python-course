"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print 
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
check_str = 'bob'
count = 0

# First check if given string is greater than the matching word
if len(s) >= len(check_str):

    # now traverse the entire length of the string to find 3 digit word
    for i in range(len(s)):

        # now check if the next 3 elements are equal to matched string
        if s[i:i+3] == check_str:
            count = count+1
    print('Number of times bob occurs is: ', count)
