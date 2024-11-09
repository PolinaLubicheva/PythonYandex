#Задание A
print(''.join(set(input())))   
     

#Задание B
print(''.join(set(input()).intersection(set(input()))))
     

#Задание C
obj = []
for _ in range(int(input())):
    obj.extend(input().split())
print('\n'.join(set(obj)))
     

#Задание D
a = int(input())
b = int(input())
sem = set()
oat = set()
for _ in range(a):
    sem.add(input())
for _ in range(b):
    oat.add(input())
both = len(sem & oat)
print(both if both else 'Таких нет')
     

#Задание E
a = int(input())
b = int(input())
p = []
for _ in range(a + b):
    p.append(input())
c = len([i for i in p if p.count(i) == 1])
print(c if c else 'Таких нет')
     

#Задание F
a = int(input())
b = int(input())
p = []
for _ in range(a + b):
    if (x := input()) not in p:
        p.append(x)
    else:
        p.remove(x)
if len(p):
    for ch in sorted(p):
        print(ch)
else:
    print('Таких нет')
     

#Задание G
morze = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K':
         '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
for char in input():
    if char != ' ':
        print(morze[char.upper()], end=' ')
    else:
        print()
     

#Задание H
a = int(input())
ks = []
for _ in range(a):
    ks.extend([input().split()])
ks.sort()
key = input()
count = 0
for k in ks:
    if key in k[1:]:
        print(k[0])
        count += 1
if not count:
    print('Таких нет')
     

#Задание I
d = {}
while x := input().split():
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
for j in d:
    print(j, d[j])
     

#Задание J
alph = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
for i in (x := input()):
    if i.upper() in alph:
        print(alph[i.upper()].lower().capitalize() if i == i.upper() else alph[i.upper()].lower(), end='')
    else:
        print(i, end='')
     

#Задание K
ppl = []
for _ in range(int(input())):
    ppl.append(input())
print(len([i for i in ppl if ppl.count(i) > 1]))
     

#Задание L
ppl = []
for _ in range(int(input())):
    ppl.append(input())
ppl = [i + ' - ' + str(ppl.count(i)) for i in set(ppl) if ppl.count(i) > 1]
if ppl:
    for x in sorted(ppl):
        print(x)
else:
    print('Однофамильцев нет')
     

#Задание M
menu = set()
new = set()
for _ in range(int(input())):
    menu.add(input())
for _ in range(int(input())):
    for j in range(int(input())):
        new.add(input())
d = sorted(menu - new)
if d:
    for dish in d:
        print(dish)
else:
    print('Готовить нечего')
     

#Задание N
ingr = []
dishes = set()
for _ in range(int(input())):
    ingr.append(input())
for _ in range(int(input())):
    dishes.add(x := input())
    for i in range(int(input())):
        if input() not in ingr:
            dishes.discard(x)
if dishes:
    for dish in sorted(dishes):
        print(dish)
else:
    print('Готовить нечего')
     

#Задание O
data = []
for i in list(map(lambda x: bin(int(x))[2:], input().split())):
    data.append({"digits": len(i),
                 "units": i.count('1'),
                 "zeros": i.count('0')})
print(data)
     

#Задание P
line = set()
while x := input().split():
    for ind, i in enumerate(x):
        if i == 'зайка' and ind not in (0, len(x) - 1):
            line.add(x[ind - 1])
            line.add(x[ind + 1])
        elif i == 'зайка' and not ind:
            line.add(x[ind + 1])
        elif i == 'зайка' and ind == len(x) - 1:
            line.add(x[ind - 1])
for item in line:
    print(item)
     

#Задание Q
friends = {}
while pair := input():
    friend1, friend2 = pair.split()
    friends[friend1] = friends.get(friend1, set()) | set([friend2])
    friends[friend2] = friends.get(friend2, set()) | set([friend1])
fof = {}
for name in sorted(friends):
    for person in friends[name]:
        fof[name] = fof.get(
            name, set()) | friends[person]
for name in fof:
    fof[name].discard(name)
    fof[name] -= friends[name]
    fof[name] = sorted(fof[name])
    print(f'{name}: {", ".join(fof[name])}')
     

#Задание R
n = {}
for _ in range(int(input())):
    x = input().split()
    if not (m := f'{x[0][:-1]}-{x[1][:-1]}') in n:
        n[m] = 1
    else:
        n[m] += 1
print(max(n.values()))
     

#Задание S
data = []
for _ in range(int(input())):
    k = list(map(lambda x: x.rstrip(','), input().split()))
    data.extend(set(k[1:]))
data = sorted(toy for toy in data if data.count(toy) == 1)
for kid in data:
    print(kid)
     

#Задание T
data = sorted(map(int, input().split('; ')))
res = dict.fromkeys(data)
for i in data:
    for j in data:
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            if res[i]:
                res[i].add(j)
            else:
                res[i] = {j}
for number in res:
    if res[number]:
        print(f'{number} - {", ".join(map(str, sorted(res[number])))}')
     