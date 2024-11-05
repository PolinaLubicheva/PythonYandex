{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Режим ожидания...\n",
      "Режим ожидания...\n",
      "Ёлочка, гори!\n"
     ]
    }
   ],
   "source": [
    "#Задача A\n",
    "count = input()\n",
    "while count != 'Три!':\n",
    "    print('Режим ожидания...')\n",
    "    count = input()\n",
    "print('Ёлочка, гори!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#Задача B\n",
    "num = 0\n",
    "while (line := str(input())) != 'Приехали!':\n",
    "    if 'зайка' in line:\n",
    "        num += 1        \n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 10 "
     ]
    }
   ],
   "source": [
    "#Задача C\n",
    "fn = int(input())\n",
    "sn = int(input())\n",
    "    while fn != sn + 1:\n",
    "        print(fn, end=' ')\n",
    "        fn += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "883.0\n"
     ]
    }
   ],
   "source": [
    "#Задача D\n",
    "fn = int(input())\n",
    "sn = int(input())\n",
    "if fn < sn:\n",
    "    while fn != sn + 1:\n",
    "        print(fn, end=' ')\n",
    "        fn += 1\n",
    "else:\n",
    "    while fn != sn - 1:\n",
    "        print(fn, end=' ')\n",
    "        fn -= 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача E\n",
    "c = 0\n",
    "while (p := float(input())) != 0:\n",
    "    if p >= 500:\n",
    "        c += p * 0.9\n",
    "    else:\n",
    "        c += p\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "#Задача F\n",
    "a = int(input())\n",
    "b = int(input())\n",
    "while a != 0 and b != 0:\n",
    "    if a > b:\n",
    "        a = a % b\n",
    "    else:\n",
    "        b = b % a\n",
    "print(a + b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "320000\n"
     ]
    }
   ],
   "source": [
    "#Задача G\n",
    "a = int(input())\n",
    "b = int(input())\n",
    "mx = max(a, b)\n",
    "while (mx % min(a, b) != 0):\n",
    "    mx += max(a, b)\n",
    "print(mx)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Нельзя нажимать неизвестные кнопки!\n",
      "Нельзя нажимать неизвестные кнопки!\n",
      "Нельзя нажимать неизвестные кнопки!\n",
      "Нельзя нажимать неизвестные кнопки!\n",
      "Нельзя нажимать неизвестные кнопки!\n",
      "Нельзя нажимать неизвестные кнопки!\n"
     ]
    }
   ],
   "source": [
    "#Задача H\n",
    "line = input()\n",
    "N = int(input())\n",
    "k = 0\n",
    "while k != N:\n",
    "    print(line)\n",
    "    k += 1 \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "#Задача I\n",
    "a = int(input())\n",
    "k = 1\n",
    "ans = 1\n",
    "while k != a + 1:\n",
    "    ans *= k\n",
    "    k += 1\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "#Задача J\n",
    "x = 0\n",
    "y = 0\n",
    "while (n := str(input())) != 'СТОП':\n",
    "    k = int(input())\n",
    "    if n == 'СЕВЕР':\n",
    "        x += k\n",
    "    if n == 'ЮГ':\n",
    "        x -= k\n",
    "    if n == 'ЗАПАД':\n",
    "        y -= k\n",
    "    if n == 'ВОСТОК':\n",
    "        y += k\n",
    "print(f'{x}\\n{y}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача K\n",
    "n = int(input())\n",
    "s = 0\n",
    "while n % 10 != 0 or n >= 10:\n",
    "    s += n % 10\n",
    "    n = n // 10\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача L\n",
    "n = int(input())\n",
    "a = n % 10\n",
    "b = 0\n",
    "while n % 10 != 0 or n >= 10:\n",
    "    b = n // 10 % 10\n",
    "    if b > a:\n",
    "        a = b \n",
    "    n = n // 10\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача M\n",
    "n = int(input())\n",
    "ans = 'Яяя'\n",
    "for i in range(0, n):\n",
    "    name = str(input())\n",
    "    if ans > name:\n",
    "        ans = name\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача N\n",
    "n = int(input())\n",
    "i = 2\n",
    "res = 'YES'\n",
    "if n > 1:\n",
    "    while n % i:\n",
    "        if i > n ** 0.5:\n",
    "            break\n",
    "        i += 1\n",
    "    else:\n",
    "        res = 'NO'\n",
    "else:\n",
    "    res = 'NO'\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача O\n",
    "n = int(input())\n",
    "k = 0\n",
    "for i in range(0, n):\n",
    "    s = input()\n",
    "    if 'зайка' in s:\n",
    "        k += 1\n",
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача P\n",
    "num = int(input())\n",
    "orig = num\n",
    "rvrs = 0\n",
    "while num > 0:\n",
    "    dg = num % 10\n",
    "    rvrs = rvrs * 10 + dg\n",
    "    num //= 10\n",
    "if orig == rvrs:\n",
    "    print('YES')\n",
    "else:\n",
    "    print('NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача Q\n",
    "num = int(input())\n",
    "res = 0\n",
    "pw = 1\n",
    "while num > 0:\n",
    "    if num % 2 != 0:\n",
    "        res += (num % 10) * pw\n",
    "        power *= 10\n",
    "    num //= 10\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача R\n",
    "num = int(input())\n",
    "if num == 1:\n",
    "    print(num)\n",
    "k = 2\n",
    "while num >= 2:\n",
    "    p = True\n",
    "    while k ** 2 <= num and p is True:\n",
    "        if num % k == 0:\n",
    "            p = False\n",
    "        else:\n",
    "            k = k + 1\n",
    "    if p is True:\n",
    "        print(num)\n",
    "        num = 1\n",
    "    else:\n",
    "        print(f'{k}', end=' * ')\n",
    "        num = num // k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача S\n",
    "start = 1\n",
    "end = 1001\n",
    "print((start + end) // 2)\n",
    "while (x := input()) != 'Угадал!':\n",
    "    if x == 'Меньше':\n",
    "        end = (start + end) // 2\n",
    "        print((start + end) // 2)\n",
    "    elif x == 'Больше':\n",
    "        start = (start + end) // 2\n",
    "        print((start + end) // 2)\n",
    "print('=' * 35)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "#Задача T\n",
    "res = -1\n",
    "n = 0\n",
    "for i in range(int(input())):\n",
    "    b = int(input())\n",
    "    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2\n",
    "    t = ((m + r + n) * 37) % 256\n",
    "    if t != h or h > 99:\n",
    "        res = i\n",
    "        break\n",
    "    n = h\n",
    "print(res)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
