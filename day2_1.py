eachLine = input()
counter, wrongPass, totIn = 0, 0, 1

while True:
    lower = int(eachLine[0 : eachLine.find('-')])
    upper = int(eachLine[(eachLine.find('-') + 1) : eachLine.find(' ')])
    letterToCount = eachLine[eachLine.find(' ') + 1]
    passToCheck = eachLine[(eachLine.find(' ') + 4):]

    if  lower <= passToCheck.count(letterToCount) <= upper:
        #print('found one')
        counter += 1

    #print(lower, upper, letterToCount, passToCheck)




    eachLine = input()
    totIn += 1
    if eachLine == '':
        break

print(counter, totIn - 1)