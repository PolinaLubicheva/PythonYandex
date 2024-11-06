{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "print(''.join(set(input())))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "print(''.join(set(input()).intersection(set(input()))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "obj = []\n",
    "for _ in range(int(input())):\n",
    "    obj.extend(input().split())\n",
    "print('\\n'.join(set(obj)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "a = int(input())\n",
    "b = int(input())\n",
    "sem = set()\n",
    "oat = set()\n",
    "for _ in range(a):\n",
    "    sem.add(input())\n",
    "for _ in range(b):\n",
    "    oat.add(input())\n",
    "both = len(sem & oat)\n",
    "print(both if both else 'Таких нет')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "a = int(input())\n",
    "b = int(input())\n",
    "p = []\n",
    "for _ in range(a + b):\n",
    "    p.append(input())\n",
    "c = len([i for i in p if p.count(i) == 1])\n",
    "print(c if c else 'Таких нет')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "a = int(input())\n",
    "b int(input())\n",
    "p = []\n",
    "for _ in range(a + b):\n",
    "    if (x := input()) not in p:\n",
    "        p.append(x)\n",
    "    else:\n",
    "        p.remove(x)\n",
    "if len(p):\n",
    "    for ch in sorted(p):\n",
    "        print(ch)\n",
    "else:\n",
    "    print('Таких нет')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "morze = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',\n",
    "         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K':\n",
    "         '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',\n",
    "         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',\n",
    "         'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',\n",
    "         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',\n",
    "         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}\n",
    "for char in input():\n",
    "    if char != ' ':\n",
    "        print(morze[char.upper()], end=' ')\n",
    "    else:\n",
    "        print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "a = int(input())\n",
    "ks = []\n",
    "for _ in range(a):\n",
    "    ks.extend([input().split()])\n",
    "ks.sort()\n",
    "key = input()\n",
    "count = 0\n",
    "for k in ks:\n",
    "    if key in k[1:]:\n",
    "        print(k[0])\n",
    "        count += 1\n",
    "if not count:\n",
    "    print('Таких нет')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "d = {}\n",
    "while x := input().split():\n",
    "    for i in x:\n",
    "        if i not in d:\n",
    "            d[i] = 1\n",
    "        else:\n",
    "            d[i] += 1\n",
    "for j in d:\n",
    "    print(j, d[j])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "alph = {\n",
    "    'А': 'A', 'Б': 'B', 'В': 'V',\n",
    "    'Г': 'G', 'Д': 'D', 'Е': 'E',\n",
    "    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',\n",
    "    'И': 'I', 'Й': 'I', 'К': 'K',\n",
    "    'Л': 'L', 'М': 'M', 'Н': 'N',\n",
    "    'О': 'O', 'П': 'P', 'Р': 'R',\n",
    "    'С': 'S', 'Т': 'T', 'У': 'U',\n",
    "    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',\n",
    "    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',\n",
    "    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',\n",
    "    'Я': 'IA', 'Ь': '', 'Ъ': '',\n",
    "}\n",
    "for i in (x := input()):\n",
    "    if i.upper() in alph:\n",
    "        print(alph[i.upper()].lower().capitalize() if i == i.upper() else alph[i.upper()].lower(), end='')\n",
    "    else:\n",
    "        print(i, end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание K\n",
    "ppl = []\n",
    "for _ in range(int(input())):\n",
    "    ppl.append(input())\n",
    "print(len([i for i in ppl if ppl.count(i) > 1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание L\n",
    "ppl = []\n",
    "for _ in range(int(input())):\n",
    "    ppl.append(input())\n",
    "ppl = [i + ' - ' + str(ppl.count(i)) for i in set(ppl) if ppl.count(i) > 1]\n",
    "if ppl:\n",
    "    for x in sorted(ppl):\n",
    "        print(x)\n",
    "else:\n",
    "    print('Однофамильцев нет')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание M\n",
    "menu = set()\n",
    "new = set()\n",
    "for _ in range(int(input())):\n",
    "    menu.add(input())\n",
    "for _ in range(int(input())):\n",
    "    for j in range(int(input())):\n",
    "        new.add(input())\n",
    "d = sorted(menu - new)\n",
    "if d:\n",
    "    for dish in d:\n",
    "        print(dish)\n",
    "else:\n",
    "    print('Готовить нечего')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание N\n",
    "ingr = []\n",
    "dishes = set()\n",
    "for _ in range(int(input())):\n",
    "    ingr.append(input())\n",
    "for _ in range(int(input())):\n",
    "    dishes.add(x := input())\n",
    "    for i in range(int(input())):\n",
    "        if input() not in ingr:\n",
    "            dishes.discard(x)\n",
    "if dishes:\n",
    "    for dish in sorted(dishes):\n",
    "        print(dish)\n",
    "else:\n",
    "    print('Готовить нечего')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание O\n",
    "data = []\n",
    "for i in list(map(lambda x: bin(int(x))[2:], input().split())):\n",
    "    data.append({\"digits\": len(i),\n",
    "                 \"units\": i.count('1'),\n",
    "                 \"zeros\": i.count('0')})\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание P\n",
    "line = set()\n",
    "while x := input().split():\n",
    "    for ind, i in enumerate(x):\n",
    "        if i == 'зайка' and ind not in (0, len(x) - 1):\n",
    "            line.add(x[ind - 1])\n",
    "            line.add(x[ind + 1])\n",
    "        elif i == 'зайка' and not ind:\n",
    "            line.add(x[ind + 1])\n",
    "        elif i == 'зайка' and ind == len(x) - 1:\n",
    "            line.add(x[ind - 1])\n",
    "for item in line:\n",
    "    print(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание Q\n",
    "friends = {}\n",
    "while pair := input():\n",
    "    friend1, friend2 = pair.split()\n",
    "    friends[friend1] = friends.get(friend1, set()) | set([friend2])\n",
    "    friends[friend2] = friends.get(friend2, set()) | set([friend1])\n",
    "fof = {}\n",
    "for name in sorted(friends):\n",
    "    for person in friends[name]:\n",
    "        fof[name] = fof.get(\n",
    "            name, set()) | friends[person]\n",
    "for name in fof:\n",
    "    fof[name].discard(name)\n",
    "    fof[name] -= friends[name]\n",
    "    fof[name] = sorted(fof[name])\n",
    "    print(f'{name}: {\", \".join(fof[name])}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание R\n",
    "n = {}\n",
    "for _ in range(int(input())):\n",
    "    x = input().split()\n",
    "    if not (m := f'{x[0][:-1]}-{x[1][:-1]}') in n:\n",
    "        n[m] = 1\n",
    "    else:\n",
    "        n[m] += 1\n",
    "print(max(n.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание S\n",
    "data = []\n",
    "for _ in range(int(input())):\n",
    "    k = list(map(lambda x: x.rstrip(','), input().split()))\n",
    "    data.extend(set(k[1:]))\n",
    "data = sorted(toy for toy in data if data.count(toy) == 1)\n",
    "for kid in data:\n",
    "    print(kid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание T\n",
    "data = sorted(map(int, input().split('; ')))\n",
    "res = dict.fromkeys(data)\n",
    "for i in data:\n",
    "    for j in data:\n",
    "        a, b = i, j\n",
    "        while b:\n",
    "            a, b = b, a % b\n",
    "        if a == 1:\n",
    "            if res[i]:\n",
    "                res[i].add(j)\n",
    "            else:\n",
    "                res[i] = {j}\n",
    "for number in res:\n",
    "    if res[number]:\n",
    "        print(f'{number} - {\", \".join(map(str, sorted(res[number])))}')"
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
