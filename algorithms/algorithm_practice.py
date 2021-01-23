# A file to practice algorithms
# Based on Andy Harris lecture
# https://youtu.be/azcrPFhaY9k?t=1886
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


# PROGRAM 2
# Display the word Hello horizontally and then vertically

# create variable for greeting
greeting = 'Hello'

# create variable for first letter
firstLetter = greeting[0]

# create variable for second letter
secondLetter = greeting[1]

# create variable for third letter
thirdLetter = greeting[2]

# create variable for fourth letter
fourthLetter = greeting[3]

# create variable for fifth letter
fifthLetter = greeting[4]


# print greeting
print(greeting)

# print first letter
print(firstLetter)

# print second letter
print(secondLetter)

# print third letter
print(thirdLetter)

# print fourth letter
print(fourthLetter)

# print fifth letter
print(fifthLetter)
