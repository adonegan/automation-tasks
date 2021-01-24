# A file to practise algorithms
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


# PROGRAM 3
# Return number of vowels in a given string

def get_count(inputStr):
    # initial counter variable
    num_vowels = 0

    # for every character in the input string
    for char in inputStr:

        # if the character is in my vowel string
        if char in 'aeiou':
            
            # increment num_vowels by 1
            num_vowels += 1
    
    # return updated variable
    return num_vowels

# print the results of the input if input is 'hiii'
print(get_count('hiii'))
# output is 3


# PROGRAM 4
# Codewars: Square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    # convert input to str 
    # rename in new variable
    x = str(num)
    # create empty list for squared digits
    squaredList = []
    # for every digit in x
    # convert to int, square it, store in new variable
    # convert that variable into a string
    # append string digits to squaredList
    for digit in x:
        squared = int(digit) ** 2
        squared = str(squared)
        squaredList.append(squared)
    # join string digits
    # store in new variable
    concatSquared = ''.join(squaredList)
    # return new variable in int format
    return int(concatSquared)

print(square_digits(9191))