{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "def recursive_sum(*args):\n",
    "    if not args:\n",
    "        return 0\n",
    "    return args[0] + recursive_sum(*args[1:])    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "def recursive_digit_sum(n):\n",
    "    return n % 10 + recursive_digit_sum(n // 10) if n else 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "def make_equation(*args):\n",
    "    if len(args) == 1:\n",
    "        return str(args[0])\n",
    "    line = ') * x ' + ('- ' if args[-1] < 0 else '+ ') + str(args[-1])\n",
    "    return '(' + make_equation(*args[:-1]) + line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "def answer(func):\n",
    "    def wrap(*args, **kwargs):\n",
    "        return f'Результат функции: {func(*args, **kwargs)}'\n",
    "    return wrap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "def result_accumulator(func):\n",
    "    result = []\n",
    "\n",
    "    def wrap(*args, method=\"accumulate\"):\n",
    "        result.append(func(*args))\n",
    "        if method == \"drop\":\n",
    "            temp = result.copy()\n",
    "            result.clear()\n",
    "            return temp\n",
    "    return wrap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "def merge_sort(arr):\n",
    "    n = len(arr)\n",
    "    if n <= 1:\n",
    "        return arr\n",
    "    else:\n",
    "        middle = int(len(arr) / 2)\n",
    "        left = merge_sort(arr[:middle])\n",
    "        right = merge_sort(arr[middle:])\n",
    "        return merge(left, right)\n",
    "        \n",
    "\n",
    "def merge(left, right):\n",
    "    result = []\n",
    "    while len(left) > 0 and len(right) > 0:\n",
    "        if left[0] <= right[0]:\n",
    "            result.append(left[0])\n",
    "            left = left[1:]\n",
    "        else:\n",
    "            result.append(right[0])\n",
    "            right = right[1:]\n",
    "    if len(left) > 0:\n",
    "        result += left\n",
    "    if len(right) > 0:\n",
    "        result += right\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "def same_type(func):\n",
    "    def wrapper(*args):\n",
    "        if len({type(i) for i in args}) != 1:\n",
    "            print(\"Обнаружены различные типы данных\")\n",
    "            return False\n",
    "        return func(*args)\n",
    "    return wrapper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "def fibonacci(n):\n",
    "    n1, n2 = 0, 1\n",
    "    for i in range(n):\n",
    "        yield n1\n",
    "        n1, n2 = n2, n1 + n2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "def cycle(line):\n",
    "    while line:\n",
    "        for i in line:\n",
    "            yield i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "def make_linear(arr):\n",
    "    new_arr = []\n",
    "    for i in arr:\n",
    "        if isinstance(i, list):\n",
    "            new_arr.extend(make_linear(i))\n",
    "        else:\n",
    "            new_arr.append(i)\n",
    "    return new_arr"
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
