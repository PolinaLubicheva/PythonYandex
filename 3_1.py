{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "for _ in range(int(input())):\n",
    "    if (word := input())[0] not in 'абв':\n",
    "        print('NO')\n",
    "        break\n",
    "else:\n",
    "    print('YES') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "for i in input():\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "length = int(input())\n",
    "for _ in range(int(input())):\n",
    "    line = input()\n",
    "    print(line[:length - 3].ljust(length, \".\") if len(line) > length else line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "while (n := input()):\n",
    "    if not n.endswith('@@@'):\n",
    "        if n.startswith('##'):\n",
    "            print(n[2:])\n",
    "        else:\n",
    "            print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "print('YES' if (line := input()) == line[::-1] else 'NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "counter = 0\n",
    "for _ in range(int(input())):\n",
    "    counter += input().count(\"зайка\")\n",
    "print(counter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "print(sum(map(int, input().split())))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "for _ in range(int(input())):\n",
    "    if \"зайка\" in (place := input()):\n",
    "        print(place.index(\"зайка\") + 1)\n",
    "    else:\n",
    "        print(\"Заек нет =(\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "while (n := input()):\n",
    "    if not n.startswith('#'):\n",
    "        print(n[:(n.index('#') if '#' in n else len(n))])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "data = []\n",
    "while (n := input()) != 'ФИНИШ':\n",
    "    data.extend(n.lower().split())\n",
    "max_count, data = 0, ''.join(data)\n",
    "for symbol in set(data):\n",
    "    max_count = max(max_count, data.count(symbol))\n",
    "print(min([i for i in set(data) if data.count(i) == max_count]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание K\n",
    "headings = []\n",
    "for _ in range(int(input())):\n",
    "    headings.append(input())\n",
    "word = input()\n",
    "for heading in headings:\n",
    "    if word.lower() in heading.lower():\n",
    "        print(heading)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание L\n",
    "order = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')\n",
    "for i in range(int(input())):\n",
    "    print(order[i % len(order)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание M\n",
    "data = []\n",
    "for _ in range(int(input())):\n",
    "    data.append(int(input()))\n",
    "number = int(input())\n",
    "for i in data:\n",
    "    print(i ** number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание N\n",
    "data = list(map(int, input().split()))\n",
    "number = int(input())\n",
    "for i in data:\n",
    "    print(i ** number, end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание O\n",
    "numbers = list(map(int, input().split()))\n",
    "a = numbers[0]\n",
    "while len(numbers) > 1:\n",
    "    b = numbers[1]\n",
    "    while b:\n",
    "        a, b = b, a % b\n",
    "    numbers.pop(1)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание P\n",
    "length, line = int(input()), []\n",
    "for _ in range(int(input())):\n",
    "    line.append(input())\n",
    "for i in line:\n",
    "    if length > 3:\n",
    "        print(i[:length - 3] + \"...\" if len(i) >= length - 3 else (i + \"...\" if length == 4 else i))\n",
    "        length -= len(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание Q\n",
    "line = ''.join(input().lower().split())\n",
    "print('YES' if line == line[::-1] else 'NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание R\n",
    "line = input()\n",
    "temp_line, repeat = line[0], 1\n",
    "for i in line[1:]:\n",
    "    if i == temp_line:\n",
    "        repeat += 1\n",
    "    else:\n",
    "        print(temp_line, repeat)\n",
    "        temp_line, repeat = i, 1\n",
    "print(temp_line, repeat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание S\n",
    "data = list(input().split())\n",
    "result = [int(data[0])]\n",
    "for i in data[1:]:\n",
    "    if i.isdigit():\n",
    "        result.append(int(i))\n",
    "    else:\n",
    "        a = result.pop()\n",
    "        exec(\"result[-1] \" + i + \"= a\")\n",
    "print(result[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание T\n",
    "exp = input()\n",
    "tk = exp.split()\n",
    "u = ['~', '#', '!']\n",
    "d = ['+', '-', '*', '/']\n",
    "t = ['@']\n",
    "operators = u + d + t\n",
    "st = []\n",
    "while tk != []:\n",
    "    token = tk.pop(0)\n",
    "    if token in u:\n",
    "        a = st.pop()\n",
    "        match token:\n",
    "            case '~':\n",
    "                st.append(-a)\n",
    "            case '!':\n",
    "                res = 1\n",
    "                for i in range(1, a + 1):\n",
    "                    res *= i\n",
    "                st.append(res)\n",
    "            case '#':\n",
    "                st.append(a)\n",
    "                st.append(a)\n",
    "    elif token in d:\n",
    "        a = st.pop()\n",
    "        b = st.pop()\n",
    "        match token:\n",
    "            case '+':\n",
    "                st.append(b + a)\n",
    "            case '-':\n",
    "                st.append(b - a)\n",
    "            case '*':\n",
    "                st.append(b * a)\n",
    "            case '/':\n",
    "                st.append(b // a)\n",
    "    elif token in t:\n",
    "        a = st.pop()\n",
    "        b = st.pop()\n",
    "        c = st.pop()\n",
    "        match token:\n",
    "            case '@':\n",
    "                st.append(b)\n",
    "                st.append(a)\n",
    "                st.append(c)\n",
    "    else:\n",
    "        st.append(int(token))\n",
    "print(int(st[-1]))"
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
