#Задание A
for _ in range(int(input())):
    if (word := input())[0] not in 'абв':
        print('NO')
        break
else:
    print('YES') 
     

#Задание B
for i in input():
    print(i)
     

#Задание C
length = int(input())
for _ in range(int(input())):
    line = input()
    print(line[:length - 3].ljust(length, ".") if len(line) > length else line)
     

#Задание D
while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)
     

#Задание E
print('YES' if (line := input()) == line[::-1] else 'NO')
     

#Задание F
counter = 0
for _ in range(int(input())):
    counter += input().count("зайка")
print(counter)
     

#Задание G
print(sum(map(int, input().split())))
     

#Задание H
for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")
     

#Задание I
while (n := input()):
    if not n.startswith('#'):
        print(n[:(n.index('#') if '#' in n else len(n))])
     

#Задание J
data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))
     

#Задание K
headings = []
for _ in range(int(input())):
    headings.append(input())
word = input()
for heading in headings:
    if word.lower() in heading.lower():
        print(heading)
     

#Задание L
order = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
for i in range(int(input())):
    print(order[i % len(order)])
     

#Задание M
data = []
for _ in range(int(input())):
    data.append(int(input()))
number = int(input())
for i in data:
    print(i ** number)
     

#Задание N
data = list(map(int, input().split()))
number = int(input())
for i in data:
    print(i ** number, end=' ')
     

#Задание O
numbers = list(map(int, input().split()))
a = numbers[0]
while len(numbers) > 1:
    b = numbers[1]
    while b:
        a, b = b, a % b
    numbers.pop(1)
print(a)
     

#Задание P
length, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)
     

#Задание Q
line = ''.join(input().lower().split())
print('YES' if line == line[::-1] else 'NO')
     

#Задание R
line = input()
temp_line, repeat = line[0], 1
for i in line[1:]:
    if i == temp_line:
        repeat += 1
    else:
        print(temp_line, repeat)
        temp_line, repeat = i, 1
print(temp_line, repeat)
     

#Задание S
data = list(input().split())
result = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        result.append(int(i))
    else:
        a = result.pop()
        exec("result[-1] " + i + "= a")
print(result[0])
     

#Задание T
exp = input()
tk = exp.split()
u = ['~', '#', '!']
d = ['+', '-', '*', '/']
t = ['@']
operators = u + d + t
st = []
while tk != []:
    token = tk.pop(0)
    if token in u:
        a = st.pop()
        match token:
            case '~':
                st.append(-a)
            case '!':
                res = 1
                for i in range(1, a + 1):
                    res *= i
                st.append(res)
            case '#':
                st.append(a)
                st.append(a)
    elif token in d:
        a = st.pop()
        b = st.pop()
        match token:
            case '+':
                st.append(b + a)
            case '-':
                st.append(b - a)
            case '*':
                st.append(b * a)
            case '/':
                st.append(b // a)
    elif token in t:
        a = st.pop()
        b = st.pop()
        c = st.pop()
        match token:
            case '@':
                st.append(b)
                st.append(a)
                st.append(c)
    else:
        st.append(int(token))
print(int(st[-1]))
     