numOne = int(input())
numTwo = int(input())
iOne = 0
kOne = 0
iTwo = 0
kTwo = 0
s = 0
while numOne != 0:
    if numOne % 2 == 0:
        numOne = numOne // 2
        iOne = iOne + 1
        kOne = kOne + 1
    elif numOne % 2 == 1:
        numOne = numOne // 2
        kOne = kOne + 1
while numTwo != 0:
    if numTwo % 2 == 0:
        iTwo = iTwo + 1
        numTwo = numTwo // 2
        kTwo = kTwo + 1
    elif numTwo % 2 == 1:
        kTwo = kTwo + 1
        numTwo = numTwo // 2
if kOne > kTwo:
    s = s + 1
elif kOne < kTwo:
    s = s + 1
if iOne > iTwo:
    s = s + (iOne - iTwo)
else:
    s = s + (iTwo - iOne)
print(s)
