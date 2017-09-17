
### This one might take some additional time to understand. Apologies. I'm a beginner ###
### To quickly understand the working of the code, insert print(i,j,s[i]) in line-9 and print(fx, '\n') in line-16 and run it###

# In a string s, in which, s = '1.2,2.34,6.7,6.7,5.2', Write a program that prints the sum of the numbers in
# the string

s = '1.2,2.34,6.7,6.7,5.2'

# 'i' will be used to store the number of iterations in the for loop
i = 0

# 'j' will be used to store the address of commas from the string and for extracting the starting of the number
# This will be used to add numbers after the first comma
j = 0

# 'fx' is the used to store the extracted number parts in the string which are converted to floating point numbers
fx = 0
fx = float(fx)

for x in s:

    # this code executes when the for loop encounters a comma
    if s[i] == ',':

        # this code executes when i is at a comma and assigns it to j at line 33.
        # This will be used to add numbers after the first comma
        if s[j] == ',':
            j = j + 1

        # this code slices the numbers from the string, converts them to a float and adds the previous value of
        # to the new sliced float
        fx = float(s[j: i]) + fx

        # this code assigns the address of the comma that this if loop is about
        j = i

    # this code adds 1 to our iteration
    i = i + 1

# After there are no commas remaining in the string, the left over values will be converted and added here
fx = float(s[j + 1:len(s)]) + fx

print(fx)

