""" Julia Siodaro AC 6
Engenharia de software turma tarde
"""

# exercício 1

print("hello world!")

# exercício 2

a = int(input())
b = int(input())

x = a + b

print("x =", x)

# exercício 3

dados1 = input()
dados2 = input()

dados1 = dados1.split(" ")
dados2 = dados2.split(" ")

preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
print(f"VALOR A PAGAR: R$ {preco:.2f}")

# exercício 4

infos = input()

infos = infos.split(" ")

a , b, c = int(infos[0]), int(infos[1]), int(infos[2])

def formula(a, b):
    return (a + b + abs(a-b)) / 2

maior = formula(a, b)

maior = formula(maior, c)

print(f"{int(maior)} é o maior.")

# exercício 5

valores1 = input()
valores2 = input()

valores1 = valores1.split()
valores2 = valores2.split()

x1, y1 = map(float, valores1)
x2, y2 = map(float, valores2)


import math
calculo_formula = math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)

print (f'{calculo_formula:.4f}')


