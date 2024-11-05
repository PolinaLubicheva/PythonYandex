{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Как Вас зовут?\n",
      "Здравствуйте, Аня!\n",
      "Как дела?\n",
      "Я за вас рада!\n"
     ]
    }
   ],
   "source": [
    "#Задача A\n",
    "print('Как Вас зовут?')\n",
    "username = input()\n",
    "print(f'''Здравствуйте, {username}!\n",
    "Как дела?''')\n",
    "answer = input()\n",
    "if 'орошо' in answer:\n",
    "    print('Я за вас рада!')\n",
    "else: \n",
    "    print('Всё наладится')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вася\n"
     ]
    }
   ],
   "source": [
    "#Задача B\n",
    "PS = int(input())\n",
    "VS = int(input())\n",
    "if PS > VS: \n",
    "    print('Петя')\n",
    "elif PS < VS:\n",
    "    print ('Вася')\n",
    "else:\n",
    "    print('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вася\n"
     ]
    }
   ],
   "source": [
    "#Задача C\n",
    "PS = int(input())\n",
    "VS = int(input())\n",
    "AS = int(input())\n",
    "MX = max(PS, VS, AS)\n",
    "if PS == MX:\n",
    "    print('Петя')\n",
    "elif VS == MX:\n",
    "    print('Вася')\n",
    "else: \n",
    "     print('Толя')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Толя\n",
      "2. Вася\n",
      "3. Петя\n"
     ]
    }
   ],
   "source": [
    "#Задача D\n",
    "PS = int(input())\n",
    "VS = int(input())\n",
    "AS = int(input())\n",
    "MX = max(PS, VS, AS)\n",
    "MN = min(PS, VS, AS)\n",
    "if PS == MX:\n",
    "    pl1 = 'Петя'\n",
    "    if AS == MN:\n",
    "        pl2 = 'Вася'\n",
    "        pl3 = 'Толя'\n",
    "    else:\n",
    "        pl2 = 'Толя'\n",
    "        pl3 = 'Вася' \n",
    "elif VS == MX:\n",
    "    pl1 = 'Вася'\n",
    "    if AS == MN:\n",
    "        pl2 = 'Петя'\n",
    "        pl3 = 'Толя'\n",
    "    else:\n",
    "        pl2 = 'Толя'\n",
    "        pl3 = 'Петя'\n",
    "else:\n",
    "    pl1 = 'Толя'\n",
    "    if PS == MN: \n",
    "        pl2 = 'Вася'\n",
    "        pl3 = 'Петя'\n",
    "    else: \n",
    "        pl2 = 'Петя'\n",
    "        pl3 = 'Вася'\n",
    "print(f'''1. {pl1}\n",
    "2. {pl2}\n",
    "3. {pl3}''')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вася\n"
     ]
    }
   ],
   "source": [
    "#Задача E\n",
    "N = int(input())\n",
    "M = int(input())\n",
    "NP = (6 + N)\n",
    "MV = (9 + M)\n",
    "if NP > MV:\n",
    "    print('Петя')\n",
    "elif NP < MV:\n",
    "    print('Вася')\n",
    "else:\n",
    "    print('Одинаково')"
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
      "YES\n"
     ]
    }
   ],
   "source": [
    "#Задача F\n",
    "year = int(input())\n",
    "if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):\n",
    "      print('YES')\n",
    "else:\n",
    "    print('NO')"
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
      "YES\n"
     ]
    }
   ],
   "source": [
    "#Задача G\n",
    "N = str(input())\n",
    "a = N[::-1]\n",
    "if N == a:\n",
    "    print('YES')\n",
    "else:\n",
    "    print('NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NO\n"
     ]
    }
   ],
   "source": [
    "#Задача H\n",
    "env = input()\n",
    "if 'зайк' in env:\n",
    "    print('YES')\n",
    "else: \n",
    "    print('NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Вася\n"
     ]
    }
   ],
   "source": [
    "#Задача I\n",
    "A = input()\n",
    "B = input()\n",
    "C = input()\n",
    "print(min(A, B, C))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "115\n"
     ]
    }
   ],
   "source": [
    "#Задача J\n",
    "pwd = int(input())\n",
    "add1 = (pwd % 10 + pwd // 10 % 10)\n",
    "add2 = ((pwd // 10 % 10) + (pwd // 100 % 10))\n",
    "if add1 > add2:\n",
    "    print(f'{add1}' + f'{add2}')\n",
    "else:\n",
    "    print(f'{add2}' + f'{add1}')"
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
      "NO\n"
     ]
    }
   ],
   "source": [
    "#Задача K\n",
    "N = int(input())\n",
    "a = (N // 100 % 10)\n",
    "b = (N // 10 % 10)\n",
    "c = (N % 10)\n",
    "MX = max(a, b, c)\n",
    "MN = min(a, b, c)\n",
    "MD = a + b + c - MX - MN\n",
    "if MX + MN == MD * 2:\n",
    "    print('YES')\n",
    "else: \n",
    "    print('NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NO\n"
     ]
    }
   ],
   "source": [
    "#Задача L\n",
    "A = int(input())\n",
    "B = int(input())\n",
    "C = int(input())\n",
    "if A + B > C and A + C > B and C + B > A:\n",
    "    print('YES')\n",
    "else: \n",
    "    print('NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача M\n",
    "E = int(input())\n",
    "D = int(input())\n",
    "H = int(input())\n",
    "if E // 10 == D // 10 == H // 10:\n",
    "    print(E // 10)\n",
    "elif E % 10 == D % 10 == H % 10:\n",
    "    print(E % 10)\n",
    "else: \n",
    "    print('NO')"
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
      "77 87 \n"
     ]
    }
   ],
   "source": [
    "#Задача N\n",
    "N = int(input())\n",
    "a = N // 100 % 10\n",
    "b = N // 10 % 10\n",
    "c = N  % 10\n",
    "MN = min(a, b, c)\n",
    "MX = max(a, b, c)\n",
    "MD = a + b + c - MN - MX\n",
    "print(f'{MD}{MN} {MX}{MD}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача O\n",
    "FN = int(input())\n",
    "SN = int(input())\n",
    "a = FN // 10\n",
    "b = FN % 10\n",
    "c = SN // 10\n",
    "d = SN % 10\n",
    "MN = min(a, b, c, d)\n",
    "MX = max(a, b, c, d)\n",
    "MD = (a + b + c + d - MN - MX) % 10\n",
    "print(MX * 100 + MD * 10 + MN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача P\n",
    "PS = int(input())\n",
    "VS = int(input())\n",
    "AS = int(input())\n",
    "g = 'I'\n",
    "s = 'II'\n",
    "b = 'III'\n",
    "MX = max(PS, VS, AS)\n",
    "MN = min(PS, VS, AS)\n",
    "if PS == MX:\n",
    "    pl1 = 'Петя'\n",
    "    if AS == MN:\n",
    "        pl2 = 'Вася'\n",
    "        pl3 = 'Толя'\n",
    "    else:\n",
    "        pl2 = 'Толя'\n",
    "        pl3 = 'Вася' \n",
    "elif VS == MX:\n",
    "    pl1 = 'Вася'\n",
    "    if AS == MN:\n",
    "        pl2 = 'Петя'\n",
    "        pl3 = 'Толя'\n",
    "    else:\n",
    "        pl2 = 'Толя'\n",
    "        pl3 = 'Петя'\n",
    "else:\n",
    "    pl1 = 'Толя'\n",
    "    if PS == MN: \n",
    "        pl2 = 'Вася'\n",
    "        pl3 = 'Петя'\n",
    "    else: \n",
    "        pl2 = 'Петя'\n",
    "        pl3 = 'Вася'\n",
    "print(f'''{pl1:^25}\n",
    "{pl2:^8}\n",
    "{pl3:>22}''')\n",
    "print(f'{s:^8} {g:^6} {b:^8}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача Q\n",
    "a = float(input()) \n",
    "b = float(input()) \n",
    "c = float(input()) \n",
    "D = b ** 2 - 4 * a * c\n",
    "if (a == 0):\n",
    "    if b == 0 and c == 0:\n",
    "        print('Infinite solutions')\n",
    "    elif c != 0 and b == 0:\n",
    "        print('No solution') \n",
    "    elif b != 0 and c == 0:\n",
    "        x1 = 0\n",
    "        print(f'{x1:.2f}')\n",
    "    elif b != 0 and c != 0:\n",
    "        x1 = - c / b\n",
    "        print(f'{x1:.2f}')\n",
    "elif a != 0:\n",
    "    if D < 0:\n",
    "        print('No solution')\n",
    "    if D == 0: \n",
    "        x1 = - b / (2 * a)\n",
    "        print(f'{x1:.2f}')\n",
    "    if D > 0:\n",
    "        x1 = (- b + D ** 0.5) / (2 * a) \n",
    "        x2 = (- b - D ** 0.5) / (2 * a)\n",
    "        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача R\n",
    "a = int(input())\n",
    "b = int(input())\n",
    "c = int(input())\n",
    "mn = min(a, b, c)\n",
    "mx = max(a, b, c)\n",
    "md = a + b + c - mn - mx\n",
    "if md ** 2 + mn ** 2 == mx ** 2:\n",
    "    print('100%')\n",
    "elif md ** 2 + mn ** 2 > mx ** 2:\n",
    "    print('крайне мала')\n",
    "else:\n",
    "    print('велика')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача S\n",
    "x = float(input())\n",
    "y = float(input())\n",
    "c = (x ** 2 + y ** 2) ** 0.5\n",
    "p = (0.25 * (x ** 2)) + (0.5 * x) * 8.75\n",
    "if x >= 0 and y >= 0:\n",
    "    if c <= 5:\n",
    "        print('Опасность! Покиньте зону как можно скорее!')\n",
    "    elif c > 10:\n",
    "        print('Вы вышли в море и рискуете быть съеденным акулой!')\n",
    "    else:\n",
    "        print('Зона безопасна. Продолжайте работу.')\n",
    "elif x <= 0 and y >= 0:\n",
    "    if y <= 5 and y <= ((5 * x) + 35) / 3:\n",
    "        print('Опасность! Покиньте зону как можно скорее!')\n",
    "    elif c > 10:\n",
    "        print('Вы вышли в море и рискуете быть съеденным акулой!')\n",
    "    else:\n",
    "        print('Зона безопасна. Продолжайте работу.')\n",
    "elif (x <= 0 and y <= 0) or (x >= 0 and y <= 0):\n",
    "    if y < p:\n",
    "        print('Опасность! Покиньте зону как можно скорее!')\n",
    "    elif c > 10:\n",
    "        print('Вы вышли в море и рискуете быть съеденным акулой!')\n",
    "    else:\n",
    "        print('Зона безопасна. Продолжайте работу.')\n",
    "elif c == 0 and y == 0:\n",
    "    print('Опасность! Покиньте зону как можно скорее!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задача T\n",
    "line_1 = str(input())\n",
    "line_2 = str(input())\n",
    "line_3 = str(input())\n",
    "lth = 1000\n",
    "line = 'яяя'\n",
    "if 'зайка' in line_1:\n",
    "    line = line_1\n",
    "    lth = len(line_1)\n",
    "if 'зайка' in line_2 and line_2 < line:\n",
    "    line = line_2\n",
    "    lth = len(line_2) \n",
    "if 'зайка' in line_3 and line_3 < line:\n",
    "    line = line_3\n",
    "    lth = len(line_3) \n",
    "print(line, lth) "
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
