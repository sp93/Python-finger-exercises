
# takes numbers from users and prints out the greatest number

# takes input
x = input('A number please: ')
y = input('Another number please: ')
z = input('A last number please: ')

x = float(x)
y = float(y)
z = float(z)

# tests the numbers against each other and prints the greater
if (x > y and x > z):
    print('{} is greater than {} and {}'.format(x, y, z))

elif (y > x and y > z):
    print('{} is greater than {} and {}'.format(y, x, z))

elif (z > y and z > x):
    print('{} is greater than {} and {}'.format(z, x, y))
