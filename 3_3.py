#Задание A
[number ** 2 for number in range(a, b + 1)]   
     

#Задание B
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]
     

#Задание C
[len(word) for word in sentence.split()]
     

#Задание D
{number for number in numbers if number % 2}
     

#Задание E
{number for number in numbers if number in [i ** 2 for i in range(1, int(max(numbers) ** 0.5 + 1))]}
     

#Задание F
{letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}
     

#Задание G
{number: [i for i in range(1, number + 1) if not number % i] for number in numbers}
     

#Задание H
''.join(word[0] for word in string.split()).upper()
     

#Задание I
' - '.join(str(i) for i in sorted(set(numbers)))
     

#Задание J
''.join(i * j for i, j in rle)
     