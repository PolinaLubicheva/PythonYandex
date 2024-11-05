{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача A\n",
    "for i in range(1, (x := int(input())) + 1):\n",
    "    for j in range(1, x + 1):\n",
    "        if j < x:\n",
    "            print(i * j, end=' ')\n",
    "        else:\n",
    "            print(i * j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача B\n",
    "for i in range(1, (x := int(input())) + 1):\n",
    "    for j in range(1, x + 1):\n",
    "        print(f'{j} * {i} = {i * j}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача C\n",
    "n = int(input())\n",
    "count = 1\n",
    "num = 1\n",
    "while num <= n:\n",
    "    for i in range(count):\n",
    "        if num > n:\n",
    "            break\n",
    "        print(num, end=' ')\n",
    "        num += 1\n",
    "    print()\n",
    "    count += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача D\n",
    "count = int(input())\n",
    "N = 0\n",
    "for _ in range(count):\n",
    "    number = int(input())\n",
    "    while number > 0:\n",
    "        N += number % 10\n",
    "        number //= 10\n",
    "print(N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача E\n",
    "counter = 0\n",
    "tp = 0\n",
    "for _ in range(int(input())):\n",
    "    while (x := input()) != 'ВСЁ':\n",
    "        if x == 'зайка':\n",
    "            tp += 1\n",
    "    if tp:\n",
    "        counter += 1\n",
    "        tp = 0\n",
    "print(counter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача F\n",
    "n = int(input())\n",
    "a = int(input())\n",
    "for _ in range(n - 1):\n",
    "    b = int(input())\n",
    "    while b:\n",
    "        a, b = b, a % b\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача G\n",
    "for i in range(int(input())):\n",
    "    for s in range(3 + i, 0, -1):\n",
    "        print(f'До старта {s} секунд(ы)')\n",
    "    print(f'Старт {i + 1}!!!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача H\n",
    "count = int(input())\n",
    "name = ''\n",
    "num = 0\n",
    "for i in range(count):\n",
    "    name2 = input()\n",
    "    number = int(input())\n",
    "    res = 0\n",
    "    while number > 0:\n",
    "        res += number % 10\n",
    "        number //= 10\n",
    "    if res >= num:\n",
    "        num = res\n",
    "        name = name2\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача I\n",
    "N = ''\n",
    "for _ in range(int(input())):\n",
    "    N += max(input())\n",
    "print(N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача J\n",
    "for i in range(1, (n := int(input())) - 1):\n",
    "    if i == 1:\n",
    "        print('А Б В')\n",
    "    for k in range(1, n - i):\n",
    "        print(f'{i} {k} {n - i - k}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача K\n",
    "count = 0\n",
    "for i in range(int(input())):\n",
    "    k = 2\n",
    "    if (n := int(input())) > 1:\n",
    "        count += 1\n",
    "        if n == 2:\n",
    "            count += 1\n",
    "        while n % k:\n",
    "            if k > n ** 0.5:\n",
    "                break\n",
    "            k += 1\n",
    "        else:\n",
    "            count -= 1\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача L\n",
    "height = int(input())\n",
    "width = int(input())\n",
    "box_width = len(str(height * width))\n",
    "for i in range(1, height + 1):\n",
    "    for k in range(width * (i - 1) + 1, width * i + 1):\n",
    "        print(f'{k:>{box_width}}', end=' ')\n",
    "        if k == width * i:\n",
    "            print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача M\n",
    "height = int(input())\n",
    "width = int(input())\n",
    "box_width = len(str(height * width))\n",
    "for i in range(1, height + 1):\n",
    "    for k in range(i, i + height * (width - 1) + 1, height):\n",
    "        print(f'{k:>{box_width}}', end=' ')\n",
    "        if k == i + height * (width - 1):\n",
    "            print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача N\n",
    "height = int(input())\n",
    "width = int(input())\n",
    "box_width = len(str(width * height))\n",
    "if height > 0 and width > 0:\n",
    "    for rw in range(height):\n",
    "        for column in range(width):\n",
    "            if (rw % 2) == 0:\n",
    "                num = rw * width + column + 1\n",
    "            else:\n",
    "                num = (rw + 1) * width - column\n",
    "            print(f'{num:>{box_width}}', end=' ')\n",
    "        print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача O\n",
    "height = int(input())\n",
    "width = int(input())\n",
    "box_width = len(str(width * height))\n",
    "for rw in range(height):\n",
    "    for column in range(width):\n",
    "        if column % 2 == 0:\n",
    "            num = column * height + rw + 1\n",
    "        else:\n",
    "            num = (column + 1) * height - rw\n",
    "        print(f'{num:>{box_width}}', end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача P\n",
    "size = int(input())\n",
    "width = int(input())\n",
    "string_length = size * width + (size - 1)\n",
    "for rw in range(size):\n",
    "    for column in range(size):\n",
    "        print(f'{((rw + 1) * (column + 1)): ^{width}}', end='')\n",
    "        if column == size - 1:\n",
    "            print()\n",
    "        else:\n",
    "            print('|', end='')\n",
    "    if rw + 1 != size:\n",
    "        print('-' * string_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача Q\n",
    "count = 0\n",
    "for _ in range(int(input())):\n",
    "    n = int(input())\n",
    "    orig = n\n",
    "    reverse = 0\n",
    "    while n > 0:\n",
    "        dg = n % 10\n",
    "        reverse = reverse * 10 + dg\n",
    "        n //= 10\n",
    "    if orig == reverse:\n",
    "        count += 1\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача R\n",
    "lim = int(input())\n",
    "counter = 0\n",
    "width = 1\n",
    "mx_length = 0\n",
    "while counter <= lim:\n",
    "    string_length = 0\n",
    "    for pos in range(width):\n",
    "        counter += 1\n",
    "        if counter <= lim:\n",
    "            string_length += len(str(counter))\n",
    "        if pos < width - 1 and counter < lim:\n",
    "            string_length += 1\n",
    "    if mx_length < string_length:\n",
    "        mx_length = string_length\n",
    "    width += 1\n",
    "counter = 0\n",
    "width = 1\n",
    "while counter <= lim:\n",
    "    string = ''\n",
    "    for pos in range(width):\n",
    "        counter += 1\n",
    "        if counter <= lim:\n",
    "            string += str(counter)\n",
    "        if pos < width - 1 and counter < lim:\n",
    "            string += ' '\n",
    "    width += 1\n",
    "    print(f'{string:^{mx_length}}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача S\n",
    "n = int(input())\n",
    "box_width = len(str((n + 1) // 2))\n",
    "for i in range(n):\n",
    "    for k in range(n):\n",
    "        print(f'{min(i + 1, k + 1, n - i, n - k):>{box_width}}', end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача T\n",
    "number = int(input())\n",
    "value = 0\n",
    "base = 0\n",
    "for base2 in range(10, 1, -1):\n",
    "    res = 0\n",
    "    num = number\n",
    "    while num > 0:\n",
    "        res += (num % base2)\n",
    "        num //= base2\n",
    "    if res >= value:\n",
    "        value = res\n",
    "        base = base2\n",
    "print(base)"
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
