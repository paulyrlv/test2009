num = int(input())
i = 2
if num == 1:
    print('1 = 1')
while 1 == 1:
    if num % i == 0:
        break
    else:
        i = i + 1
if num == i:
    print(num, '=', num)
else:
    print(num, ' = ', num // i, '*', i)
