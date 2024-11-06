{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "def print_hello(name):\n",
    "    print(f'Hello, {name}!')  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "def gcd(a, b):\n",
    "    while b:\n",
    "        a, b = b, a % b\n",
    "    return a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "def number_length(number):\n",
    "    return len(str(abs(number)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "def month(number, language):\n",
    "    MONTH = {\n",
    "        'en': [\n",
    "            'January', 'February', 'March',\n",
    "            'April', 'May', 'June',\n",
    "            'July', 'August', 'September',\n",
    "            'October', 'November', 'December'\n",
    "        ],\n",
    "        'ru': [\n",
    "            'Январь', 'Февраль', 'Март',\n",
    "            'Апрель', 'Май', 'Июнь',\n",
    "            'Июль', 'Август', 'Сентябрь',\n",
    "            'Октябрь', 'Ноябрь', 'Декабрь'\n",
    "        ]\n",
    "    }\n",
    "    return MONTH[language][number - 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "def split_numbers(line):\n",
    "    return tuple(map(int, line.split()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "lst = []\n",
    "def modern_print(string):\n",
    "    print(string) if string not in lst else None\n",
    "    lst.append(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "def can_eat(horse, shape):\n",
    "    return abs(horse[0] - shape[0]) + abs(horse[1] - shape[1]) == 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "def is_palindrome(n):\n",
    "    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "def is_prime(n):\n",
    "    for i in range(2, int(n**0.5) + 1):\n",
    "        if not n % i:\n",
    "            return False\n",
    "    return n != 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "def merge(a, b):\n",
    "    c = list(a) + list(b)\n",
    "    n = len(c)\n",
    "    for i in range(n):\n",
    "        for j in range(0, n - i - 1):\n",
    "            if c[j] > c[j + 1]:\n",
    "                c[j], c[j + 1] = c[j + 1], c[j]\n",
    "    return tuple(c)"
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
