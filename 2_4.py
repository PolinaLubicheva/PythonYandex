#Задача A
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        if j < x:
            print(i * j, end=' ')
        else:
            print(i * j)
     
#Задача B
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        print(f'{j} * {i} = {i * j}')
     
#Задача C
n = int(input())
count = 1
num = 1
while num <= n:
    for i in range(count):
        if num > n:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1
     
#Задача D
count = int(input())
N = 0
for _ in range(count):
    number = int(input())
    while number > 0:
        N += number % 10
        number //= 10
print(N)
     
#Задача E
counter = 0
tp = 0
for _ in range(int(input())):
    while (x := input()) != 'ВСЁ':
        if x == 'зайка':
            tp += 1
    if tp:
        counter += 1
        tp = 0
print(counter)
     
#Задача F
n = int(input())
a = int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
print(a)
     

#Задача G
for i in range(int(input())):
    for s in range(3 + i, 0, -1):
        print(f'До старта {s} секунд(ы)')
    print(f'Старт {i + 1}!!!')
     
#Задача H
count = int(input())
name = ''
num = 0
for i in range(count):
    name2 = input()
    number = int(input())
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    if res >= num:
        num = res
        name = name2
print(name)
     
#Задача I
N = ''
for _ in range(int(input())):
    N += max(input())
print(N)
     
#Задача J
for i in range(1, (n := int(input())) - 1):
    if i == 1:
        print('А Б В')
    for k in range(1, n - i):
        print(f'{i} {k} {n - i - k}')    

#Задача K
count = 0
for i in range(int(input())):
    k = 2
    if (n := int(input())) > 1:
        count += 1
        if n == 2:
            count += 1
        while n % k:
            if k > n ** 0.5:
                break
            k += 1
        else:
            count -= 1
print(count)

#Задача L
height = int(input())
width = int(input())
box_width = len(str(height * width))
for i in range(1, height + 1):
    for k in range(width * (i - 1) + 1, width * i + 1):
        print(f'{k:>{box_width}}', end=' ')
        if k == width * i:
            print()

#Задача M
height = int(input())
width = int(input())
box_width = len(str(height * width))
for i in range(1, height + 1):
    for k in range(i, i + height * (width - 1) + 1, height):
        print(f'{k:>{box_width}}', end=' ')
        if k == i + height * (width - 1):
            print()    

#Задача N
height = int(input())
width = int(input())
box_width = len(str(width * height))
if height > 0 and width > 0:
    for rw in range(height):
        for column in range(width):
            if (rw % 2) == 0:
                num = rw * width + column + 1
            else:
                num = (rw + 1) * width - column
            print(f'{num:>{box_width}}', end=' ')
        print()

#Задача O
height = int(input())
width = int(input())
box_width = len(str(width * height))
for rw in range(height):
    for column in range(width):
        if column % 2 == 0:
            num = column * height + rw + 1
        else:
            num = (column + 1) * height - rw
        print(f'{num:>{box_width}}', end=' ')
    print()

#Задача P
size = int(input())
width = int(input())
string_length = size * width + (size - 1)
for rw in range(size):
    for column in range(size):
        print(f'{((rw + 1) * (column + 1)): ^{width}}', end='')
        if column == size - 1:
            print()
        else:
            print('|', end='')
    if rw + 1 != size:
        print('-' * string_length)

#Задача Q
count = 0
for _ in range(int(input())):
    n = int(input())
    orig = n
    reverse = 0
    while n > 0:
        dg = n % 10
        reverse = reverse * 10 + dg
        n //= 10
    if orig == reverse:
        count += 1
print(count)   

#Задача R
lim = int(input())
counter = 0
width = 1
mx_length = 0
while counter <= lim:
    string_length = 0
    for pos in range(width):
        counter += 1
        if counter <= lim:
            string_length += len(str(counter))
        if pos < width - 1 and counter < lim:
            string_length += 1
    if mx_length < string_length:
        mx_length = string_length
    width += 1
counter = 0
width = 1
while counter <= lim:
    string = ''
    for pos in range(width):
        counter += 1
        if counter <= lim:
            string += str(counter)
        if pos < width - 1 and counter < lim:
            string += ' '
    width += 1
    print(f'{string:^{mx_length}}')

#Задача S
n = int(input())
box_width = len(str((n + 1) // 2))
for i in range(n):
    for k in range(n):
        print(f'{min(i + 1, k + 1, n - i, n - k):>{box_width}}', end=' ')
    print()
     
#Задача T
number = int(input())
value = 0
base = 0
for base2 in range(10, 1, -1):
    res = 0
    num = number
    while num > 0:
        res += (num % base2)
        num //= base2
    if res >= value:
        value = res
        base = base2
print(base)