# Get input from the user
# Take 10 variables and assign input methods as values which take an int

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = int(input('1st integer: ')), int(input('2nd integer: ')), int(
    input('3rd integer: ')), int(input('4th integer: ')), \
                                          int(input('5th integer: ')), int(input('6th integer: ')), int(
    input('7th integer: ')), int(input('8th integer: ')), \
                                          int(input('9th integer: ')), int(input('10th integer: '))

# Even/Odd filtering
# Variables for storing odd integers
o1, o2, o3, o4, o5, o6, o7, o8, o9, o10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

# Filtering odd integers by ensuring that their values have been added to the 'o' variables.
# If a number is even, an 'o' won't have it's value be replaced by it whereas an odd integer's value will replace an 'o'-
# -which initially has a value of zero
if x1 % 2 == 1:
    o1 = x1

if x2 % 2 == 1:
    o2 = x2

if x3 % 2 == 1:
    o3 = x3

if x4 % 2 == 1:
    o4 = x4

if x5 % 2 == 1:
    o5 = x5

if x6 % 2 == 1:
    o6 = x6

if x7 % 2 == 1:
    o7 = x7

if x8 % 2 == 1:
    o8 = x8

if x9 % 2 == 1:
    o9 = x9

if x10 % 2 == 1:
    o10 = x10

# Now values have been assigned to odd integers we'll compare them against one another.
# This works because, all evens have a value of 0 and odd ones have their original input value.

if o1 > o10 and o1 > o2 and o1 > o3 and o1 > o4 and o1 > o5 and o1 > o6 and o1 > o7 and o1 > o8 and o1 > o9:
    print(o1, 'is your largest odd integer')

elif o2 > o1 and o2 > o3 and o2 > o4 and o2 > o5 and o2 > o6 and o2 > o7 and o2 > o8 and o2 > o9 and o2 > o10:
    print(o2, 'is your largest odd integer')

elif o3 > o1 and o3 > o2 and o3 > o4 and o3 > o5 and o3 > o6 and o3 > o7 and o3 > o8 and o3 > o9 and o3 > o10:
    print(o3, 'is your largest odd integer')

elif o4 > o1 and o4 > o2 and o4 > o3 and o4 > o5 and o4 > o6 and o4 > o7 and o4 > o8 and o4 > o9 and o4 > o10:
    print(o4, 'is your largest odd integer')

elif o5 > o1 and o5 > o2 and o5 > o3 and o5 > o4 and o5 > o6 and o5 > o7 and o5 > o8 and o5 > o9 and o5 > o10:
    print(o5, 'is your largest odd integer')

elif o6 > o1 and o6 > o2 and o6 > o3 and o6 > o4 and o6 > o5 and o6 > o7 and o6 > o8 and o6 > o9 and o6 > o10:
    print(o6, 'is your largest odd integer')

elif o7 > o1 and o7 > o2 and o7 > o3 and o7 > o4 and o7 > o5 and o7 > o6 and o7 > o8 and o7 > o9 and o7 > o10:
    print(o7, 'is your largest odd integer')

elif o8 > o1 and o8 > o2 and o8 > o3 and o8 > o4 and o8 > o5 and o8 > o7 and o8 > o6 and o8 > o9 and o8 > o10:
    print(o8, 'is your largest odd integer')

elif o9 > o1 and o9 > o2 and o9 > o3 and o9 > o4 and o9 > o5 and o9 > o7 and o9 > o6 and o9 > o8 and o9 > o10:
    print(o9, 'is your largest odd integer')

elif o10 > o1 and o10 > o2 and o10 > o3 and o10 > o4 and o10 > o5 and o10 > o6 and o10 > o7 and o10 > o8 and o10 > o9:
    print(o10, 'is your largest odd integer')

elif x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 == 0 and x4 % 2 == 0 and x5 % 2 == 0 and x6 % 2 == 0 and x7 % 2 == 0 \
        and x8 % 2 == 0 and x9 % 2 == 0 and x10 % 2 == 0:
    print('All even integers.')
