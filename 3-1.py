# Get an integer and output it's root and power such that root raised to the power equals the input integer and 0 < power < 6.
# Get an integer as an input from the user
new_Integer = int(input('An integer please: '))

# Create variables and assign an initial value of 0 to them
r = 0
p = 0

# Create a while loop to find out the root and the power for our input
while r**p != abs(new_Integer):
    p = p + 1
    if p > 5:
        p = 0
        r = r + 1

# Output a negative root and a power, in case the input is negative
if new_Integer < 0:
    if p % 2 == 1:
        r = 0 - r
        p = 0 - p

# Print a root and a power
print('Root is:', r, 'and Power is:', p)

# Print 'no pairs' in case, the input has no root and/or power in the integer form
if r**p > abs(new_Integer):
    print('no pairs')

