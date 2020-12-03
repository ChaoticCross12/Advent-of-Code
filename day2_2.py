eachLine = input()
counter, wrongPass, totIn = 0, 0, 1

while True:
    first = int(eachLine[0 : eachLine.find('-')])
    second = int(eachLine[(eachLine.find('-') + 1) : eachLine.find(' ')])
    letterToCount = eachLine[eachLine.find(' ') + 1]
    passToCheck = eachLine[(eachLine.find(' ') + 4):]

    if  passToCheck[first - 1] == letterToCount or passToCheck[second - 1] == letterToCount:
        if not (passToCheck[first - 1] == letterToCount and passToCheck[second - 1] == letterToCount):
            counter += 1
            #print(first, second, letterToCount, passToCheck)
            #print(passToCheck[first - 1], passToCheck[second - 1])




    eachLine = input()
    totIn += 1
    if eachLine == '':
        break

print(counter, totIn - 1)