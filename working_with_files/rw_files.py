# Automating reading files and writing to files

# Reading a file
with open('file1.txt') as file:
    contents = file.readlines()
    contents = [ line.strip() for line in contents ]
    
    for line in contents:
        splittedLine = line.split()

        wordOne = splittedLine[0]
        wordTwo = splittedLine[1]
        wordThree = splittedLine[2]
        wordFour = splittedLine[3]
        wordFive = splittedLine[4]
        
        jumbledWords = wordFour + wordOne + wordThree + wordFive + wordTwo
        print(jumbledWords)
        #output = linethismy2is

# Writing to a file
with open('file2.txt', 'w') as file:
    file.write('Just me overwriting what is already in my file')

# with open('file2.txt') as file:
#     print(file.read())

# Use append instead to add text to a file
with open('file2.txt', 'a') as file:
    file.write('\nMy newly added line')

with open('file2.txt') as file:
    print(file.read())