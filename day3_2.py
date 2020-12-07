firstLine = input()
eachLine = input()
lengthOfLine = len(eachLine)
index3, index1, index5, index7, index1d2, r3d1, r1d1, r5d1, r7d1, r1d2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
thisTime = 1

while True:

    # r3d1
    if index3 + 3 < lengthOfLine:
        index3 += 3
    else:
        index3 = index3 - lengthOfLine + 3


    if eachLine[index3] == '#':
        r3d1 += 1


    # r1d1
    if index1 + 1 < lengthOfLine:
        index1 += 1
    else:
        index1 = index1 - lengthOfLine + 1


    if eachLine[index1] == '#':
        r1d1 += 1



    # r5d1
    if index5 + 5 < lengthOfLine:
        index5 += 5
    else:
        index5 = index5 - lengthOfLine + 5


    if eachLine[index5] == '#':
        r5d1 += 1



    # r7d1
    if index7 + 7 < lengthOfLine:
        index7 += 7
    else:
        index7 = index7 - lengthOfLine + 7


    if eachLine[index7] == '#':
        r7d1 += 1



    # r1d2
    if index1d2 + 1 < lengthOfLine:
        if thisTime % 2 == 0:
            index1d2 += 1

            if eachLine[index1d2] == '#':
                r1d2 += 1
    else:
        if thisTime % 2 == 0:
            index1d2 = index1d2 - lengthOfLine + 1

            if eachLine[index1d2] == '#':
                r1d2 += 1



    thisTime += 1
    eachLine = input()

    if eachLine == '':
        break


finalTreeProd = r3d1 * r1d1 * r5d1 * r7d1 * r1d2
print(finalTreeProd)
print(r3d1, r1d1, r5d1, r7d1, r1d2)