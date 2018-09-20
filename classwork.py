numOne = int(input())
numTwo = int(input())
numThree = int(input())
numOneSorted = 0
numTwoSorted = 0
numThreeSorted = 0
if (numOne > numTwo) and (numOne > numThree):
    numOneSorted = numOne
    if numTwo >= numThree:
        numTwoSorted = numTwo
        numThreeSorted = numThree
    else:
        numTwoSorted = numThree
        numThreeSorted = numTwo
elif (numTwo > numOne) and (numTwo > numThree):
    numOneSorted = numTwo
    if numOne >= numThree:
        numTwoSorted = numOne
        numThreeSorted = numThree
    else:
        numTwoSorted = numThree
        numThreeSorted = numOne
elif (numThree > numTwo) and (numThree > numOne):
    numOneSorted = numThree
    if numTwo >= numOne:
        numTwoSorted = numTwo
        numThreeSorted = numOne
    else:
        numTwoSorted = numOne
        numThreeSorted = numTwo
print(numThreeSorted, numTwoSorted, numOneSorted, sep=' ')
