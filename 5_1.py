{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "class Point:\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "class Point:\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "\n",
    "    def move(self, shift_x, shift_y):\n",
    "        self.x += shift_x\n",
    "        self.y += shift_y\n",
    "\n",
    "    def length(self, p):\n",
    "        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "class RedButton:\n",
    "    def __init__(self):\n",
    "        self.counter = 0\n",
    "\n",
    "    def click(self):\n",
    "        print('Тревога!')\n",
    "        self.counter += 1\n",
    "\n",
    "    def count(self):\n",
    "        return self.counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "class Programmer:\n",
    "\n",
    "    def __init__(self, name, position=\"Junior\"):\n",
    "        self.name = name\n",
    "        self.position = position\n",
    "        self.worked = 0\n",
    "        self.money = 0\n",
    "        self.overrises = 0\n",
    "\n",
    "    def work(self, time):\n",
    "        P = {\n",
    "            \"Junior\": 10,\n",
    "            \"Middle\": 15,\n",
    "            \"Senior\": 20,\n",
    "        }\n",
    "        self.worked += time\n",
    "        self.money += time * (P[self.position] + self.overrises)\n",
    "\n",
    "    def rise(self):\n",
    "        if self.position == \"Junior\":\n",
    "            self.position = \"Middle\"\n",
    "        elif self.position == \"Middle\":\n",
    "            self.position = \"Senior\"\n",
    "        elif self.position == \"Senior\":\n",
    "            self.overrises += 1\n",
    "\n",
    "    def info(self):\n",
    "        return f'{self.name} {self.worked}ч. {self.money}тгр.'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "class Rectangle:\n",
    "    def __init__(self, *coords):\n",
    "        self.coords = coords\n",
    "        self.first_line = abs(self.coords[0][0] - self.coords[1][0])\n",
    "        self.second_line = abs(self.coords[0][1] - self.coords[1][1])\n",
    "\n",
    "    def perimeter(self):\n",
    "        return round(2 * (self.first_line + self.second_line), 2)\n",
    "\n",
    "    def area(self):\n",
    "        return round(self.first_line * self.second_line, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "class Rectangle:\n",
    "    def __init__(self, *coords):\n",
    "        self.coords = coords\n",
    "        self.upper_left_x = round(min(self.coords[0][0], self.coords[1][0]), 2)\n",
    "        self.upper_left_y = round(max(self.coords[0][1], self.coords[1][1]), 2)\n",
    "        self.lower_right_x = round(max(self.coords[0][0], self.coords[1][0]), 2)\n",
    "        self.lower_right_y = round(min(self.coords[0][1], self.coords[1][1]), 2)\n",
    "        self.width = abs(self.coords[0][0] - self.coords[1][0])\n",
    "        self.height = abs(self.coords[0][1] - self.coords[1][1])\n",
    "\n",
    "    def perimeter(self):\n",
    "        return round(2 * (self.width + self.height), 2)\n",
    "\n",
    "    def area(self):\n",
    "        return round(self.width * self.height, 2)\n",
    "\n",
    "    def get_pos(self):\n",
    "        return self.upper_left_x, self.upper_left_y\n",
    "\n",
    "    def get_size(self):\n",
    "        return round(self.width, 2), round(self.height, 2)\n",
    "\n",
    "    def move(self, dx, dy):\n",
    "        self.coords = (self.coords[0][0] + dx, self.coords[0][1] + dy), (self.coords[1][0] + dx, self.coords[1][1] + dy)\n",
    "        self.__init__(*self.coords)\n",
    "\n",
    "    def resize(self, width, height):\n",
    "        self.coords = self.get_pos(), (self.upper_left_x + width, self.upper_left_y - height)\n",
    "        self.__init__(*self.coords)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "class Rectangle:\n",
    "    def __init__(self, coord1, coord2):\n",
    "        self.left = min(coord1[0], coord2[0])\n",
    "        self.top = max(coord1[1], coord2[1])\n",
    "        self.right = max(coord1[0], coord2[0])\n",
    "        self.bottom = min(coord1[1], coord2[1])\n",
    "        self.w = round(abs(coord1[0] - coord2[0]), 2)\n",
    "        self.h = round(abs(coord1[1] - coord2[1]), 2)\n",
    "        self.x = min(coord1[0], coord2[0])\n",
    "        self.y = max(coord1[1], coord2[1])\n",
    "        self.flag = False\n",
    "\n",
    "    def perimeter(self):\n",
    "        return round(abs(self.left - self.right) * 2 + abs(self.top - self.bottom) * 2, 2)\n",
    "\n",
    "    def area(self):\n",
    "        return round(abs(self.left - self.right) * abs(self.top - self.bottom), 2)\n",
    "\n",
    "    def get_pos(self):\n",
    "        return self.left, self.top\n",
    "\n",
    "    def get_size(self):\n",
    "        if self.flag:\n",
    "            return self.w, self.h\n",
    "        return ((round(abs(self.left - self.right), 2), round(abs(self.top - self.bottom), 2)))\n",
    "\n",
    "    def resize(self, width, height):\n",
    "        self.flag = False\n",
    "        self.right = round(self.left + width, 2)\n",
    "        self.bottom = round(self.top + height, 2)\n",
    "        self.w, self.h = width, height\n",
    "\n",
    "    def turn(self):\n",
    "        self.flag = False\n",
    "        width, height = self.get_size()\n",
    "        d = (width - height) / 2\n",
    "        self.left = round(self.left + d, 2)\n",
    "        self.right = round(self.right - d, 2)\n",
    "        self.top = round(self.top + d, 2)\n",
    "        self.bottom = round(self.bottom - d, 2)\n",
    "        d = (self.w - self.h) / 2\n",
    "        self.x = round(self.x + d, 2)\n",
    "        self.y = round(self.y + d, 2)\n",
    "        self.w, self.h = self.h, self.w\n",
    "\n",
    "    def scale(self, factor):\n",
    "        self.flag = False\n",
    "        width, height = self.get_size()\n",
    "        self.flag = False\n",
    "        if abs(width - self.w) <= 0.01:\n",
    "            width = self.w\n",
    "        if abs(height - self.h) <= 0.02:\n",
    "            height = self.h\n",
    "        self.left = round(self.left - (factor * width - width) / 2, 2)\n",
    "        self.top = round(self.top + (factor * height - height) / 2, 2)\n",
    "        width = round(width * factor, 2)\n",
    "        height = round(height * factor, 2)\n",
    "        self.right = round(self.left + width, 2)\n",
    "        self.bottom = round(self.top - height, 2)\n",
    "        self.x = round(self.x - (factor * self.w - self.w) / 2, 2)\n",
    "        self.y = round(self.y + (factor * self.h - self.h) / 2, 2)\n",
    "        self.w = round(self.w * factor, 2)\n",
    "        self.h = round(self.h * factor, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "class Checkers:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.desk = {\n",
    "            'A': {\n",
    "                '8': 'X',\n",
    "                '7': 'B',\n",
    "                '6': 'X',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'W',\n",
    "                '2': 'X',\n",
    "                '1': 'W',\n",
    "            },\n",
    "            'B': {\n",
    "                '8': 'B',\n",
    "                '7': 'X',\n",
    "                '6': 'B',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'X',\n",
    "                '2': 'W',\n",
    "                '1': 'X',\n",
    "            },\n",
    "            'C': {\n",
    "                '8': 'X',\n",
    "                '7': 'B',\n",
    "                '6': 'X',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'W',\n",
    "                '2': 'X',\n",
    "                '1': 'W',\n",
    "            },\n",
    "            'D': {\n",
    "                '8': 'B',\n",
    "                '7': 'X',\n",
    "                '6': 'B',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'X',\n",
    "                '2': 'W',\n",
    "                '1': 'X',\n",
    "            },\n",
    "            'E': {\n",
    "                '8': 'X',\n",
    "                '7': 'B',\n",
    "                '6': 'X',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'W',\n",
    "                '2': 'X',\n",
    "                '1': 'W',\n",
    "            },\n",
    "            'F': {\n",
    "                '8': 'B',\n",
    "                '7': 'X',\n",
    "                '6': 'B',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'X',\n",
    "                '2': 'W',\n",
    "                '1': 'X',\n",
    "            },\n",
    "            'G': {\n",
    "                '8': 'X',\n",
    "                '7': 'B',\n",
    "                '6': 'X',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'W',\n",
    "                '2': 'X',\n",
    "                '1': 'W',\n",
    "            },\n",
    "            'H': {\n",
    "                '8': 'B',\n",
    "                '7': 'X',\n",
    "                '6': 'B',\n",
    "                '5': 'X',\n",
    "                '4': 'X',\n",
    "                '3': 'X',\n",
    "                '2': 'W',\n",
    "                '1': 'X',\n",
    "            },\n",
    "        }\n",
    "\n",
    "    def move(self, f, t):\n",
    "        self.desk[f[0]][f[1]], self.desk[t[0]][t[1]] = self.desk[t[0]][t[1]], self.desk[f[0]][f[1]]\n",
    "\n",
    "    def get_cell(self, p):\n",
    "        return Cell(self.desk[p[0]][p[1]])\n",
    "\n",
    "\n",
    "class Cell:\n",
    "\n",
    "    def __init__(self, coords):\n",
    "        self.coords = coords\n",
    "\n",
    "    def status(self):\n",
    "        return self.coords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "class Queue:\n",
    "    a = []\n",
    "\n",
    "    def push(self, item):\n",
    "        self.a.append(item)\n",
    "\n",
    "    def pop(self):\n",
    "        return self.a.pop(0)\n",
    "\n",
    "    def is_empty(self):\n",
    "        return self.a == []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "class Stack:\n",
    "    a = []\n",
    "\n",
    "    def push(self, item):\n",
    "        self.a.append(item)\n",
    "\n",
    "    def pop(self):\n",
    "        return self.a.pop()\n",
    "\n",
    "    def is_empty(self):\n",
    "        return self.a == []"
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
