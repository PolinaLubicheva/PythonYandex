{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание A\n",
    "from sys import stdin\n",
    "print(sum(map(int, stdin.read().split())))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание B\n",
    "from sys import stdin\n",
    "print(round(sum(x := [int(i.split()[2]) - int(i.split()[1]) for i in stdin.readlines()]) / len(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание C\n",
    "from sys import stdin\n",
    "for i in stdin.readlines():\n",
    "    if not i.startswith('#'):\n",
    "        print(i[:i.find('#')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание D\n",
    "from sys import stdin\n",
    "for line in (x := [i.strip() for i in stdin])[:-1]:\n",
    "    if x[-1].lower() in line.lower():\n",
    "        print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание E\n",
    "from sys import stdin\n",
    "data = [string.strip().split() for string in stdin]\n",
    "words = []\n",
    "for line in data:\n",
    "    words.extend(line)\n",
    "for word in sorted(set(words)):\n",
    "    if word.lower() == word.lower()[::-1]:\n",
    "        print(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание F\n",
    "LITER = {\n",
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
    "data, translit_data = '', ''\n",
    "with open(\"cyrillic.txt\", encoding=\"UTF-8\") as file_in:\n",
    "    for line in file_in:\n",
    "        data += line\n",
    "\n",
    "for i in data:\n",
    "    if i.upper() in LITER:\n",
    "        translit_data += LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower()\n",
    "    else:\n",
    "        translit_data += i\n",
    "with open(\"transliteration.txt\", \"w\", encoding=\"UTF-8\") as file_out:\n",
    "    print(translit_data, file=file_out)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание G\n",
    "name = input()\n",
    "numbers = []\n",
    "with open(name, 'r') as f:\n",
    "    for line in f:\n",
    "        numbers.extend([int(x) for x in line.split()])\n",
    "print(len(numbers))\n",
    "print(len(list(filter(lambda x: x > 0, numbers))))\n",
    "print(min(numbers))\n",
    "print(max(numbers))\n",
    "print(sum(numbers))\n",
    "print(round(sum(numbers) / len(numbers), 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание H\n",
    "files_in = input(), input()\n",
    "file_out = input()\n",
    "words = [set(), set()]\n",
    "for i in range(len(files_in)):\n",
    "    with open(files_in[i], 'r') as file_in:\n",
    "        for line in file_in:\n",
    "            words[i].update({x for x in line.split()})\n",
    "with open(file_out, 'w') as file_out:\n",
    "    for word in sorted(words[0].symmetric_difference(words[1])):\n",
    "        print(word, file=file_out)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание I\n",
    "first_file, second_file = input(), input()\n",
    "data = []\n",
    "with open(first_file, 'r') as f:\n",
    "    for line in f:\n",
    "        data.append(line.strip().replace('\\t', '').split())\n",
    "data = [i for i in data if any(i)]\n",
    "with open(second_file, 'w') as g:\n",
    "    for line in data:\n",
    "        print(' '.join(line), file=g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание J\n",
    "file_in, number = input(), int(input())\n",
    "data = []\n",
    "with open(file_in) as f:\n",
    "    for line in f:\n",
    "        data.append(line)\n",
    "for line in data[-number:]:\n",
    "    print(line.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание K\n",
    "import json\n",
    "file_in, file_out = input(), input()\n",
    "numbers = []\n",
    "with open(file_in) as f:\n",
    "    for line in f:\n",
    "        numbers.extend([int(x) for x in line.split()])\n",
    "data = {\n",
    "        \"count\": len(numbers),\n",
    "        \"positive_count\": len(list(filter(lambda x: x > 0, numbers))),\n",
    "        \"min\": min(numbers),\n",
    "        \"max\": max(numbers),\n",
    "        \"sum\": sum(numbers),\n",
    "        \"average\": round(sum(numbers) / len(numbers), 2)\n",
    "}\n",
    "with open(file_out, \"w\", encoding=\"UTF-8\") as g:\n",
    "    json.dump(data, g, ensure_ascii=False, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание L\n",
    "from sys import stdin\n",
    "files = [name.strip() for name in stdin]\n",
    "data = []\n",
    "with open(files[0]) as f:\n",
    "    for line in f:\n",
    "        data.append(line.split())\n",
    "D = dict(zip([1, 2, 3], ['>', '<', '==']))\n",
    "for n in range(1, len(files)):\n",
    "    with open(files[n], 'w') as f:\n",
    "        for line in data:\n",
    "            for i in line:\n",
    "                if eval('len(list(filter(lambda x: not int(x) % 2, i)))'\n",
    "                        + D[n] +\n",
    "                        'len(list(filter(lambda x: int(x) % 2, i)))'):\n",
    "                    print(i, end=' ', file=f)\n",
    "            print('\\n', end='', file=f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание M\n",
    "from sys import stdin\n",
    "import json\n",
    "data = [line.strip() for line in stdin]\n",
    "print(data)\n",
    "print({line.split(' == ')[0]: line.split(' == ')[1] for line in data[1:]})\n",
    "D = {line.split(' == ')[0]: line.split(' == ')[1] for line in data[1:]}\n",
    "with open(data[0], 'r', encoding=\"UTF-8\") as f:\n",
    "    records = json.load(f)\n",
    "records.update(D)\n",
    "if len(data) > 1:\n",
    "    with open(data[0], 'w', encoding=\"UTF-8\") as f:\n",
    "        json.dump(records, f, ensure_ascii=False, indent=4, sort_keys=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание N\n",
    "import json\n",
    "file_1, file_2 = input(), input()\n",
    "with open(file_1, 'r') as f:\n",
    "    data_1 = json.load(f)\n",
    "with open(file_2, 'r') as f:\n",
    "    data_2 = json.load(f)\n",
    "data_1 = {i[\"name\"]: {k: v for k, v in i.items() if k != \"name\"} for i in data_1}\n",
    "for d in data_2:\n",
    "    if d[\"name\"] in data_1:\n",
    "        for key in d:\n",
    "            if (key not in data_1[d[\"name\"]] or d[key] > data_1[d[\"name\"]][key]) and key != \"name\":\n",
    "                data_1[d[\"name\"]][key] = d[key]\n",
    "    else:\n",
    "        data_1[d[\"name\"]] = {k: v for k, v in d.items() if k != \"name\"}\n",
    "with open(file_1, 'w') as g:\n",
    "    json.dump(data_1, g, ensure_ascii=False, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание O\n",
    "from sys import stdin\n",
    "import json\n",
    "answers = [i.strip() for i in stdin]\n",
    "with open(\"scoring.json\", \"r\") as file_in:\n",
    "    data = json.load(file_in)\n",
    "data = [{y[\"pattern\"]: x[\"points\"] // len(x[\"tests\"]) for y in x[\"tests\"]} for x in data]\n",
    "result, counter = 0, 0\n",
    "for i in data:\n",
    "    for j in range(counter, len(i) + counter):\n",
    "        if answers[j] in i:\n",
    "            result += i[answers[j]]\n",
    "        counter += 1\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание P\n",
    "from sys import stdin\n",
    "data = [line.strip() for line in stdin]\n",
    "query = data[0].lower()\n",
    "D = {}\n",
    "for file in data[1:]:\n",
    "    with open(file, \"r\", encoding=\"UTF-8\") as f:\n",
    "        D[file] = f.read()\n",
    "        if query in ' '.join(D[file].replace('&nbsp;', ' ').lower().split()):\n",
    "            print(file)\n",
    "        else:\n",
    "            del D[file]\n",
    "if not D:\n",
    "    print('404. Not Found')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание Q\n",
    "with open(\"secret.txt\", 'r', encoding='UTF-8') as f:\n",
    "    print(''.join([chr(ord(i) % 128) for i in f.read()]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание R\n",
    "import os\n",
    "size = os.path.getsize(input())\n",
    "if size > 1024**3 - 1:\n",
    "    size = int(size / 1024**3) + 1\n",
    "    postfix = 'ГБ'\n",
    "elif size > 1024**2 - 1:\n",
    "    size = int(size / 1024**2) + 1\n",
    "    postfix = 'МБ'\n",
    "elif size > 1023:\n",
    "    size = int(size / 1024) + 1\n",
    "    postfix = 'КБ'\n",
    "else:\n",
    "    postfix = 'Б'\n",
    "print(str(size) + postfix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание S\n",
    "shift = int(input())\n",
    "a = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "with open(\"public.txt\", \"r\", encoding=\"UTF-8\") as file_in:\n",
    "    data = file_in.read()\n",
    "data_out = [a[(a.find(i.lower()) + shift) % len(a)] if i.lower() in a else i for i in data]\n",
    "for ind, letter in enumerate(data):\n",
    "    if letter.isupper():\n",
    "        data_out[ind] = data_out[ind].upper()\n",
    "with open(\"private.txt\", \"w\") as file_out:\n",
    "    print(''.join(data_out), file=file_out)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Задание T\n",
    "with open(\"numbers.num\", \"rb\") as f:\n",
    "    data = f.read()\n",
    "print(sum([int.from_bytes(data[i:i + 2], \"big\") for i in range(0, len(data), 2)]) % 2**16)"
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
