
#Задача A
print('Как Вас зовут?')
username = input()
print(f'''Здравствуйте, {username}!
Как дела?''')
answer = input()
if 'орошо' in answer:
    print('Я за вас рада!')
else: 
    print('Всё наладится')

#Задача B
PS = int(input())
VS = int(input())
if PS > VS: 
    print('Петя')
elif PS < VS:
    print ('Вася')
else:
    print('')

#Задача C
PS = int(input())
VS = int(input())
AS = int(input())
MX = max(PS, VS, AS)
if PS == MX:
    print('Петя')
elif VS == MX:
    print('Вася')
else: 
     print('Толя')

#Задача D
PS = int(input())
VS = int(input())
AS = int(input())
MX = max(PS, VS, AS)
MN = min(PS, VS, AS)
if PS == MX:
    pl1 = 'Петя'
    if AS == MN:
        pl2 = 'Вася'
        pl3 = 'Толя'
    else:
        pl2 = 'Толя'
        pl3 = 'Вася' 
elif VS == MX:
    pl1 = 'Вася'
    if AS == MN:
        pl2 = 'Петя'
        pl3 = 'Толя'
    else:
        pl2 = 'Толя'
        pl3 = 'Петя'
else:
    pl1 = 'Толя'
    if PS == MN: 
        pl2 = 'Вася'
        pl3 = 'Петя'
    else: 
        pl2 = 'Петя'
        pl3 = 'Вася'
print(f'''1. {pl1}
2. {pl2}
3. {pl3}''')

#Задача E
N = int(input())
M = int(input())
NP = (6 + N)
MV = (9 + M)
if NP > MV:
    print('Петя')
elif NP < MV:
    print('Вася')
else:
    print('Одинаково')

#Задача F
year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      print('YES')
else:
    print('NO')

#Задача G
N = str(input())
a = N[::-1]
if N == a:
    print('YES')
else:
    print('NO')

#Задача H
env = input()
if 'зайк' in env:
    print('YES')
else: 
    print('NO')

#Задача I
A = input()
B = input()
C = input()
print(min(A, B, C))

#Задача J
pwd = int(input())
add1 = (pwd % 10 + pwd // 10 % 10)
add2 = ((pwd // 10 % 10) + (pwd // 100 % 10))
if add1 > add2:
    print(f'{add1}' + f'{add2}')
else:
    print(f'{add2}' + f'{add1}')

#Задача K
N = int(input())
a = (N // 100 % 10)
b = (N // 10 % 10)
c = (N % 10)
MX = max(a, b, c)
MN = min(a, b, c)
MD = a + b + c - MX - MN
if MX + MN == MD * 2:
    print('YES')
else: 
    print('NO')

#Задача L
A = int(input())
B = int(input())
C = int(input())
if A + B > C and A + C > B and C + B > A:
    print('YES')
else: 
    print('NO')

#Задача M
E = int(input())
D = int(input())
H = int(input())
if E // 10 == D // 10 == H // 10:
    print(E // 10)
elif E % 10 == D % 10 == H % 10:
    print(E % 10)
else: 
    print('NO')

#Задача N
N = int(input())
a = N // 100 % 10
b = N // 10 % 10
c = N  % 10
MN = min(a, b, c)
MX = max(a, b, c)
MD = a + b + c - MN - MX
print(f'{MD}{MN} {MX}{MD}')

#Задача O
FN = int(input())
SN = int(input())
a = FN // 10
b = FN % 10
c = SN // 10
d = SN % 10
MN = min(a, b, c, d)
MX = max(a, b, c, d)
MD = (a + b + c + d - MN - MX) % 10
print(MX * 100 + MD * 10 + MN)

#Задача P
PS = int(input())
VS = int(input())
AS = int(input())
g = 'I'
s = 'II'
b = 'III'
MX = max(PS, VS, AS)
MN = min(PS, VS, AS)
if PS == MX:
    pl1 = 'Петя'
    if AS == MN:
        pl2 = 'Вася'
        pl3 = 'Толя'
    else:
        pl2 = 'Толя'
        pl3 = 'Вася' 
elif VS == MX:
    pl1 = 'Вася'
    if AS == MN:
        pl2 = 'Петя'
        pl3 = 'Толя'
    else:
        pl2 = 'Толя'
        pl3 = 'Петя'
else:
    pl1 = 'Толя'
    if PS == MN: 
        pl2 = 'Вася'
        pl3 = 'Петя'
    else: 
        pl2 = 'Петя'
        pl3 = 'Вася'
print(f'''{pl1:^25}
{pl2:^8}
{pl3:>22}''')
print(f'{s:^8} {g:^6} {b:^8}')

#Задача Q
a = float(input()) 
b = float(input()) 
c = float(input()) 
D = b ** 2 - 4 * a * c
if (a == 0):
    if b == 0 and c == 0:
        print('Infinite solutions')
    elif c != 0 and b == 0:
        print('No solution') 
    elif b != 0 and c == 0:
        x1 = 0
        print(f'{x1:.2f}')
    elif b != 0 and c != 0:
        x1 = - c / b
        print(f'{x1:.2f}')
elif a != 0:
    if D < 0:
        print('No solution')
    if D == 0: 
        x1 = - b / (2 * a)
        print(f'{x1:.2f}')
    if D > 0:
        x1 = (- b + D ** 0.5) / (2 * a) 
        x2 = (- b - D ** 0.5) / (2 * a)
        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')

#Задача R
a = int(input())
b = int(input())
c = int(input())
mn = min(a, b, c)
mx = max(a, b, c)
md = a + b + c - mn - mx
if md ** 2 + mn ** 2 == mx ** 2:
    print('100%')
elif md ** 2 + mn ** 2 > mx ** 2:
    print('крайне мала')
else:
    print('велика')

#Задача S
x = float(input())
y = float(input())
c = (x ** 2 + y ** 2) ** 0.5
p = (0.25 * (x ** 2)) + (0.5 * x) * 8.75
if x >= 0 and y >= 0:
    if c <= 5:
        print('Опасность! Покиньте зону как можно скорее!')
    elif c > 10:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    else:
        print('Зона безопасна. Продолжайте работу.')
elif x <= 0 and y >= 0:
    if y <= 5 and y <= ((5 * x) + 35) / 3:
        print('Опасность! Покиньте зону как можно скорее!')
    elif c > 10:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    else:
        print('Зона безопасна. Продолжайте работу.')
elif (x <= 0 and y <= 0) or (x >= 0 and y <= 0):
    if y < p:
        print('Опасность! Покиньте зону как можно скорее!')
    elif c > 10:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    else:
        print('Зона безопасна. Продолжайте работу.')
elif c == 0 and y == 0:
    print('Опасность! Покиньте зону как можно скорее!')

#Задача T
line_1 = str(input())
line_2 = str(input())
line_3 = str(input())
lth = 1000
line = 'яяя'
if 'зайка' in line_1:
    line = line_1
    lth = len(line_1)
if 'зайка' in line_2 and line_2 < line:
    line = line_2
    lth = len(line_2) 
if 'зайка' in line_3 and line_3 < line:
    line = line_3
    lth = len(line_3) 
print(line, lth) 