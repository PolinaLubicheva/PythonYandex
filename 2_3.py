
#Задача A
count = input()
while count != 'Три!':
    print('Режим ожидания...')
    count = input()
print('Ёлочка, гори!')

#Задача B
num = 0
while (line := str(input())) != 'Приехали!':
    if 'зайка' in line:
        num += 1        
print(num)

#Задача C
fn = int(input())
sn = int(input())
while fn != sn + 1:
        print(fn, end=' ')
        fn += 1

#Задача D
fn = int(input())
sn = int(input())
if fn < sn:
    while fn != sn + 1:
        print(fn, end=' ')
        fn += 1
else:
    while fn != sn - 1:
        print(fn, end=' ')
        fn -= 1

#Задача E
c = 0
while (p := float(input())) != 0:
    if p >= 500:
        c += p * 0.9
    else:
        c += p
print(c)

#Задача F
a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)

#Задача G
a = int(input())
b = int(input())
mx = max(a, b)
while (mx % min(a, b) != 0):
    mx += max(a, b)
print(mx)
320000
#Задача H
line = input()
N = int(input())
k = 0
while k != N:
    print(line)
    k += 1 

#Задача I
a = int(input())
k = 1
ans = 1
while k != a + 1:
    ans *= k
    k += 1
print(ans)

#Задача J
x = 0
y = 0
while (n := str(input())) != 'СТОП':
    k = int(input())
    if n == 'СЕВЕР':
        x += k
    if n == 'ЮГ':
        x -= k
    if n == 'ЗАПАД':
        y -= k
    if n == 'ВОСТОК':
        y += k
print(f'{x}\n{y}')

#Задача K
n = int(input())
s = 0
while n % 10 != 0 or n >= 10:
    s += n % 10
    n = n // 10
print(s)

#Задача L
n = int(input())
a = n % 10
b = 0
while n % 10 != 0 or n >= 10:
    b = n // 10 % 10
    if b > a:
        a = b 
    n = n // 10
print(a)

#Задача M
n = int(input())
ans = 'Яяя'
for i in range(0, n):
    name = str(input())
    if ans > name:
        ans = name
print(ans)

#Задача N
n = int(input())
i = 2
res = 'YES'
if n > 1:
    while n % i:
        if i > n ** 0.5:
            break
        i += 1
    else:
        res = 'NO'
else:
    res = 'NO'
print(res)

#Задача O
n = int(input())
k = 0
for i in range(0, n):
    s = input()
    if 'зайка' in s:
        k += 1
print(k)

#Задача P
num = int(input())
orig = num
rvrs = 0
while num > 0:
    dg = num % 10
    rvrs = rvrs * 10 + dg
    num //= 10
if orig == rvrs:
    print('YES')
else:
    print('NO')

#Задача Q
num = int(input())
res = 0
pw = 1
while num > 0:
    if num % 2 != 0:
        res += (num % 10) * pw
        pw *= 10
    num //= 10
print(res)

#Задача R
num = int(input())
if num == 1:
    print(num)
k = 2
while num >= 2:
    p = True
    while k ** 2 <= num and p is True:
        if num % k == 0:
            p = False
        else:
            k = k + 1
    if p is True:
        print(num)
        num = 1
    else:
        print(f'{k}', end=' * ')
        num = num // k

#Задача S
start = 1
end = 1001
print((start + end) // 2)
while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        end = (start + end) // 2
        print((start + end) // 2)
    elif x == 'Больше':
        start = (start + end) // 2
        print((start + end) // 2)
print('=' * 35)

#Задача T
res = -1
n = 0
for i in range(int(input())):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + n) * 37) % 256
    if t != h or h > 99:
        res = i
        break
    n = h
print(res)