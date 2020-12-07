firstLine = input()
eachLine = input()
lengthOfLine = len(eachLine)
index, counterOfTrees = 0, 0


while True:

    if index + 3 < lengthOfLine:
        index += 3
    else:
        index = index - lengthOfLine + 3

    if eachLine[index] == '#':
        counterOfTrees += 1

    eachLine = input()
    
    if eachLine == '':
        break

print(counterOfTrees)