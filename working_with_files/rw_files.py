# Automating reading files and writing to files

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