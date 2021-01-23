# A file to practice algorithms
# Write algorithm on paper first
# Then convert to code

# PROGRAM 1
# Ask the user for two numbers and add them

# create an integer variable for x
# create an integer variable for y
# create an integer variable for sum
x = 0
y = 0
sum = 0

# ask the user 'x: ' and put answer in x
# ask the user 'y: ' and put answer in y
x = input('Pick a number: ')
y = input('Pick another number: ')

# convert x value to int and store in new variable
# convert y value to int and store in new variable
numX = int(x)
numY = int(y)

# add numX and numY and store in sum variable
sum = numX + numY

# tell user sum
print('The sum is... ')
print(sum)