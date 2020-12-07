validCounter = 0

while True:


    mainLine = input()
    secondLine = input()

    while secondLine != '':
        mainLine = mainLine + " " + secondLine
        secondLine = input()

    mainLine = mainLine.split()

    theDict = dict()

    for elem in mainLine:
        elem = elem.split(':')
        miniDict = dict(zip(elem[::2], elem[1::2]))
        theDict.update(miniDict)
    

    if all (key in theDict for key in ('ecl', 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid')):
        print('valid')
        validCounter += 1
    else:
        print('invalid')

    if (theDict == {}):
        print(validCounter)
        break