x = 1
y = 2
s = 2
while y < 4000000:
    print(x)
    y = y+x
    x = y-x
    if y%2 == 0:
        s = s+y
print('сумма:', s)
