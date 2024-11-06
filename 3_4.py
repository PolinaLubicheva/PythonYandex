{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "for index, word in enumerate(input().split(), start=1):\n",
    "    print(f'{index}. {word}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "for kids in zip(a := input().split(', '), b := input().split(', ')):\n",
    "    print(f'{kids[0]} - {kids[1]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "from itertools import count\n",
    "a, b, step = list(map(float, input().split()))\n",
    "for value in count(a, step):\n",
    "    if value <= b:\n",
    "        print(f'{value:.2f}')\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "from itertools import accumulate\n",
    "for value in accumulate(map(lambda x: ' ' + x, input().split())):\n",
    "    print(value[1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "items = set()\n",
    "for _ in range(3):\n",
    "    items = items.union({item for item in input().split(', ')})\n",
    "for i, item in enumerate(sorted(items), start=1):\n",
    "    print(f'{i}. {item}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "from itertools import product\n",
    "nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']\n",
    "suits = ['пик', 'треф', 'бубен', 'червей']\n",
    "suits.remove(input())\n",
    "for card in product(nominal, suits):\n",
    "    print(card[0], card[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "from itertools import product\n",
    "players, games = [], []\n",
    "for _ in range(int(input())):\n",
    "    players.append(input())\n",
    "for i in product(players, players):\n",
    "    if i[0] != i[1] and [i[1], i[0]] not in games:\n",
    "        games.append([i[0], i[1]])\n",
    "        print(f'{i[0]} - {i[1]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "M = []\n",
    "for _ in range(int(input())):\n",
    "    M.append(input())\n",
    "amount = int(input())\n",
    "M *= amount // len(M) + 1\n",
    "for i in range(amount):\n",
    "    print(M[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "from itertools import product\n",
    "for i in (n := range(1, int(input()) + 1)):\n",
    "    print(' '.join(map(lambda x: str(x[0] * x[1]), product(n, [i]))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "for i in range(1, (n := int(input())) - 1):\n",
    "    if i == 1:\n",
    "        print('А Б В')\n",
    "    for j in range(1, n - i):\n",
    "        print(f'{i} {j} {n - i - j}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание K\n",
    "from itertools import product\n",
    "n, m = int(input()), int(input())\n",
    "for i in range(n):\n",
    "    line = product(range(1, m + 1), [i * m])\n",
    "    print(' '.join(map(lambda x: str(sum(x)).rjust(len(str((n - 1 - i) * m + sum(x))), ' '), line)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание L\n",
    "items = []\n",
    "for _ in range(int(input())):\n",
    "    items.extend([item for item in input().split(', ')])\n",
    "for i, item in enumerate(sorted(items), start=1):\n",
    "    print(f'{i}. {item}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание M\n",
    "from itertools import permutations\n",
    "items = []\n",
    "for _ in range(int(input())):\n",
    "    items.append(input())\n",
    "for i in sorted(permutations(items)):\n",
    "    print(', '.join(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание N\n",
    "from itertools import permutations\n",
    "items = []\n",
    "for _ in range(int(input())):\n",
    "    items.append(input())\n",
    "for i in sorted(permutations(items, 3)):\n",
    "    print(', '.join(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание O\n",
    "from itertools import permutations\n",
    "items = []\n",
    "for _ in range(int(input())):\n",
    "    items.extend([item for item in input().split(', ')])\n",
    "for item in sorted(permutations(items, 3)):\n",
    "    print(' '.join(item))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание P\n",
    "from itertools import product, permutations\n",
    "suits_ro = [\"бубен\", \"пик\", \"треф\", \"червей\"]\n",
    "suit, exception = input(), input()\n",
    "best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]\n",
    "nominal = [\"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\", \"валет\", \"дама\", \"король\", \"туз\"]\n",
    "nominal.remove(exception)\n",
    "comb = permutations(product(sorted(nominal), sorted(suits_ro)), 3)\n",
    "y = [', '.join(' '.join(j) for j in sorted(i)) for i in comb]\n",
    "triads = [i for i in y if best_suit in i][:10]\n",
    "for triad in triads:\n",
    "    print(triad)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание Q\n",
    "from itertools import product, permutations\n",
    "suits_ro = sorted([\"бубен\", \"пик\", \"треф\", \"червей\"])\n",
    "suit, exception, situation = input(), input(), input()\n",
    "best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]\n",
    "nominal = sorted([\"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\", \"валет\", \"дама\", \"король\", \"туз\"])\n",
    "nominal.remove(exception)\n",
    "comb = permutations(product(nominal, suits_ro), 3)\n",
    "y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))\n",
    "triads = [i for i in y if best_suit in i]\n",
    "for ind, triad in enumerate(triads):\n",
    "    if triad == situation:\n",
    "        print(triads[ind + 1])\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание R\n",
    "x = input()\n",
    "print('a b c f')\n",
    "for i in range(8):\n",
    "    values = list(bin(i)[2:].zfill(3))\n",
    "    a, b, c = map(int, values)\n",
    "    print(' '.join(values), int(eval(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание S\n",
    "x = input()\n",
    "args = sorted({i for i in x if i.isupper()})\n",
    "print(' '.join(args), 'F')\n",
    "for i in range(2 ** len(args)):\n",
    "    values = list(bin(i)[2:].zfill(len(args)))\n",
    "    exec(', '.join(args) + \" = map(int, values)\")\n",
    "    print(' '.join(values), int(eval(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание T\n",
    "from itertools import product\n",
    "\n",
    "OPERATORS = {\n",
    "    'not': 'not',\n",
    "    'and': 'and',\n",
    "    'or': 'or',\n",
    "    '^': '!=',\n",
    "    '->': '<=',\n",
    "    '~': '==',\n",
    "}\n",
    "\n",
    "PRIORITY = {\n",
    "    'not': 0,\n",
    "    'and': 1,\n",
    "    'or': 2,\n",
    "    '^': 3,\n",
    "    '->': 4,\n",
    "    '~': 5,\n",
    "    '(': 6,\n",
    "}\n",
    "\n",
    "\n",
    "def parse_exp(exp, var):\n",
    "    stack = []\n",
    "    res = []\n",
    "\n",
    "    exp = exp.replace('(', '( ').replace(')', ' )')\n",
    "\n",
    "    for item in exp.split():\n",
    "        if item in var:\n",
    "            res.append(item)\n",
    "        elif item == '(':\n",
    "            stack.append(item)\n",
    "        elif item == ')':\n",
    "            while stack[-1] != '(':\n",
    "                res.append(OPERATORS[stack.pop()])\n",
    "            stack.pop()\n",
    "        elif item in OPERATORS:\n",
    "            while stack and PRIORITY[item] >= PRIORITY[stack[-1]]:\n",
    "                res.append(OPERATORS[stack.pop()])\n",
    "            stack.append(item)\n",
    "    while stack:\n",
    "        res.append(OPERATORS[stack.pop()])\n",
    "    return res\n",
    "\n",
    "\n",
    "def evaluate(exp, var):\n",
    "    stack = []\n",
    "    for item in exp:\n",
    "        if item in var:\n",
    "            stack.append(var[item])\n",
    "        else:\n",
    "            if item == 'not':\n",
    "                stack.append(not stack.pop())\n",
    "            else:\n",
    "                var2, var1 = stack.pop(), stack.pop()\n",
    "                stack.append(eval(f'{var1} {item} {var2}'))\n",
    "    return int(stack.pop())\n",
    "\n",
    "\n",
    "exp = input()\n",
    "var = sorted(set([item for item in exp if item.isupper()]))\n",
    "parsed_exp = parse_exp(exp, var)\n",
    "table = product([0, 1], repeat=len(var))\n",
    "\n",
    "print(*var, 'F')\n",
    "for values in table:\n",
    "    globals = {key: value for key, value in zip(var, values)}\n",
    "    print(*values, evaluate(parsed_exp, globals))"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
