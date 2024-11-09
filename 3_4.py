#Задание A
for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')
     

#Задание B
for kids in zip(a := input().split(', '), b := input().split(', ')):
    print(f'{kids[0]} - {kids[1]}')
     

#Задание C
from itertools import count
a, b, step = list(map(float, input().split()))
for value in count(a, step):
    if value <= b:
        print(f'{value:.2f}')
    else:
        break
     

#Задание D
from itertools import accumulate
for value in accumulate(map(lambda x: ' ' + x, input().split())):
    print(value[1:])
     

#Задание E
items = set()
for _ in range(3):
    items = items.union({item for item in input().split(', ')})
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')
     

#Задание F
from itertools import product
nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card in product(nominal, suits):
    print(card[0], card[1])
     

#Задание G
from itertools import product
players, games = [], []
for _ in range(int(input())):
    players.append(input())
for i in product(players, players):
    if i[0] != i[1] and [i[1], i[0]] not in games:
        games.append([i[0], i[1]])
        print(f'{i[0]} - {i[1]}')
     

#Задание H
M = []
for _ in range(int(input())):
    M.append(input())
amount = int(input())
M *= amount // len(M) + 1
for i in range(amount):
    print(M[i])
     

#Задание I
from itertools import product
for i in (n := range(1, int(input()) + 1)):
    print(' '.join(map(lambda x: str(x[0] * x[1]), product(n, [i]))))
     

#Задание J
for i in range(1, (n := int(input())) - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, n - i):
        print(f'{i} {j} {n - i - j}')
     

#Задание K
from itertools import product
n, m = int(input()), int(input())
for i in range(n):
    line = product(range(1, m + 1), [i * m])
    print(' '.join(map(lambda x: str(sum(x)).rjust(len(str((n - 1 - i) * m + sum(x))), ' '), line)))
     

#Задание L
items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')
     

#Задание M
from itertools import permutations
items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items)):
    print(', '.join(i))
     

#Задание N
from itertools import permutations
items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items, 3)):
    print(', '.join(i))
     

#Задание O
from itertools import permutations
items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for item in sorted(permutations(items, 3)):
    print(' '.join(item))
     

#Задание P
from itertools import product, permutations
suits_ro = ["бубен", "пик", "треф", "червей"]
suit, exception = input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]
nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
nominal.remove(exception)
comb = permutations(product(sorted(nominal), sorted(suits_ro)), 3)
y = [', '.join(' '.join(j) for j in sorted(i)) for i in comb]
triads = [i for i in y if best_suit in i][:10]
for triad in triads:
    print(triad)
     

#Задание Q
from itertools import product, permutations
suits_ro = sorted(["бубен", "пик", "треф", "червей"])
suit, exception, situation = input(), input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]
nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
nominal.remove(exception)
comb = permutations(product(nominal, suits_ro), 3)
y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))
triads = [i for i in y if best_suit in i]
for ind, triad in enumerate(triads):
    if triad == situation:
        print(triads[ind + 1])
        break
     

#Задание R
x = input()
print('a b c f')
for i in range(8):
    values = list(bin(i)[2:].zfill(3))
    a, b, c = map(int, values)
    print(' '.join(values), int(eval(x)))
     

#Задание S
x = input()
args = sorted({i for i in x if i.isupper()})
print(' '.join(args), 'F')
for i in range(2 ** len(args)):
    values = list(bin(i)[2:].zfill(len(args)))
    exec(', '.join(args) + " = map(int, values)")
    print(' '.join(values), int(eval(x)))
     

#Задание T
from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def parse_exp(exp, var):
    stack = []
    res = []

    exp = exp.replace('(', '( ').replace(')', ' )')

    for item in exp.split():
        if item in var:
            res.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack[-1] != '(':
                res.append(OPERATORS[stack.pop()])
            stack.pop()
        elif item in OPERATORS:
            while stack and PRIORITY[item] >= PRIORITY[stack[-1]]:
                res.append(OPERATORS[stack.pop()])
            stack.append(item)
    while stack:
        res.append(OPERATORS[stack.pop()])
    return res


def evaluate(exp, var):
    stack = []
    for item in exp:
        if item in var:
            stack.append(var[item])
        else:
            if item == 'not':
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f'{var1} {item} {var2}'))
    return int(stack.pop())


exp = input()
var = sorted(set([item for item in exp if item.isupper()]))
parsed_exp = parse_exp(exp, var)
table = product([0, 1], repeat=len(var))

print(*var, 'F')
for values in table:
    globals = {key: value for key, value in zip(var, values)}
    print(*values, evaluate(parsed_exp, globals))
     