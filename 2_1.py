# Задача A
print('Привет, Яндекс!')

#Задача B
print("Как Вас зовут?")
username = input()
print(f"Привет, {username}")

#Задача С
a = input()
print(f'{a}\n' * 3)

#Задача D
cash = int(input())
price = int(38 * 2.5)
print(cash - price)

#Задача E
price = int(input())
weight = int(input())
cash = int(input())
print(cash - price * weight)

#Задача F
product_name = input()
price = int(input())
weight = int(input())
cash = int(input())
print(f"Чек")
print(f'{product_name} - {weight}кг - {price}руб/кг') 
print(f"Итого: {weight * price}руб") 
print(f"Внесено: {cash}руб")
print(f"Сдача: {cash - price * weight}руб")

#Задача G
N = int(input())
print(f'Купи слона!\n' * N)

#Задача H
N = int(input())
punishment = input()
print(f'Я больше никогда не буду писать "{punishment}"!\n' * N)

#Задача I
print(int(input()) // 2 * int(input()))

#Задача J
name = input()
number = int(input())
print(f'Группа №{number // 100 % 10}.')
print(f'{number % 10}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number // 10 % 10}.')

#Задача K
num = int(input())
print(f'{num // 100 % 10}' + f'{num // 1000 % 10}' + f'{num % 10}' + f'{num // 10 % 10}')

#Задача L
first_num = int(input())
second_num = int(input())
a = ((first_num % 10) + (second_num % 10)) % 10
b = ((first_num // 10 % 10) + (second_num // 10 % 10)) % 10
c = ((first_num // 100) + (second_num // 100)) % 10
print(f'{a}{b}{c}')

#Задача M
children = int(input())
sweets = int(input())
print(int(sweets / children))
print(sweets - (int(sweets / children) * children))

#Задача N
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#Задача O
N = int(input())
M = int(input())
T = int(input())
NMT = (N * 60 + M + T)
H = int(NMT / 60)
D = int(H / 24)
N_O = (H - D * 24)
M_O = (NMT - H * 60)
print(f'{N_O:0>2}:{M_O:0>2}')

#Задача P
A = int(input())
B = int(input())
C = int(input())
print(f'{(B - A) / C:.2f}')

#Задача Q
C = int(input())
L = input('')
print(f'{C + int(L, 2)}')

#Задача R
price = input('')
cash = int(input())
print(cash - int(price, 2))

#Задача S
product_name = input()
price = int(input())
weight = int(input())
cash = int(input())
price_string = f"{weight}кг * {price}руб/кг"
print(f'''================Чек================
Товар:{product_name:>29}
Цена:{price_string:>30}
Итого: {price * weight:>25}руб
Внесено: {cash:>23}руб
Сдача: {cash - price * weight:>25}руб
===================================''')

#Задача T
N = int(input(''))
M = int(input(''))
K_1 = int(input())
K_2 = int(input())
x = ((M * N - N * K_2) / (K_1 - K_2))
y = (N - x)
print(f'{int(x)} {int(y)}')