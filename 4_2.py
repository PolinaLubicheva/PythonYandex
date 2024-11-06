{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "def make_list(length, value=0):\n",
    "    return [value] * length   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "def make_matrix(size, value=0):\n",
    "    if isinstance(size, int):\n",
    "        return [[value for i in range(size)] for j in range(size)]\n",
    "    else:\n",
    "        return [[value for i in range(size[0])] for j in range(size[1])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "def gcd(*args):\n",
    "    a = list(args)\n",
    "    while len(a) > 1:\n",
    "        while a[1]:\n",
    "            a[0], a[1] = a[1], a[0] % a[1]\n",
    "        a.pop(1)\n",
    "    return a[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "def month(number, language='ru'):\n",
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
    "def to_string(*args, **kwargs):\n",
    "    return kwargs.get(\"sep\", \" \").join([str(i) for i in args]) + kwargs.get(\"end\", \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "def order(*args):\n",
    "    temp = in_stock\n",
    "    GRADES = {\n",
    "        \"Эспрессо\": {\"coffee\": 1},\n",
    "        \"Капучино\": {\"coffee\": 1,\n",
    "                     \"milk\": 3},\n",
    "        \"Макиато\": {\"coffee\": 2,\n",
    "                    \"milk\": 1},\n",
    "        \"Кофе по-венски\": {\"coffee\": 1,\n",
    "                           \"cream\": 2},\n",
    "        \"Латте Макиато\": {\"coffee\": 1,\n",
    "                          \"milk\": 2,\n",
    "                          \"cream\": 1},\n",
    "        \"Кон Панна\": {\"coffee\": 1,\n",
    "                      \"cream\": 1},\n",
    "    }\n",
    "    for grade in args:\n",
    "        for ingr in GRADES[grade]:\n",
    "            if GRADES[grade].get(ingr, 0) > in_stock[ingr]:\n",
    "                break\n",
    "        else:\n",
    "            for ingr in GRADES[grade]:\n",
    "                in_stock[ingr] -= GRADES[grade][ingr]\n",
    "            return grade\n",
    "    if in_stock == temp:\n",
    "        return \"К сожалению, не можем предложить Вам напиток\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "numbers = tuple()\n",
    "\n",
    "\n",
    "def enter_results(*args):\n",
    "    global numbers\n",
    "    numbers += args\n",
    "\n",
    "\n",
    "def get_sum():\n",
    "    return round(sum(numbers[::2]), 2), round(sum(numbers[1::2]), 2)\n",
    "\n",
    "\n",
    "def get_average():\n",
    "    return round(2 * get_sum()[0] / len(numbers), 2), round(2 * get_sum()[1] / len(numbers), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "lambda x: (len(x), x.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "lambda x: not sum(map(int, str(x))) % 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "def secret_replace(text, **kwargs):\n",
    "    result = ''\n",
    "    kwargs = {d: (v, 0) for d, v in kwargs.items()}\n",
    "    for i in text:\n",
    "        if i in kwargs:\n",
    "            result += kwargs[i][0][kwargs[i][1] % len(kwargs[i][0])]\n",
    "            kwargs[i] = kwargs[i][0], kwargs[i][1] + 1\n",
    "        else:\n",
    "            result += i\n",
    "    return result"
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
