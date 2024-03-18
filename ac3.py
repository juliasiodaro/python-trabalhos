""" AC 3 Julia Siodaro
Engenharia de software turma tarde

"""
# exercício 1: triângulos

def determina_tipo_triângulo():
    a = int(input("Informe lado a: "))
    b = int(input("Informe lado b: "))
    c = int(input("Informe lado c: "))
    if (a + b) > c and (a + c) > c and (c + b) > a:
        if a == b == c:
            print("Triângulo equilátero.")
        elif a == b or a == c or c == b:
            print("Triângulo isósceles.")
        elif a != b or a != c or c != b:
            print("Triângulo escaleno.")
    else:
        print("Não é um triângulo.")

# determina_tipo_triângulo()

# exercício 2: dias da semana

def testa_dia_da_semana(numero):
    if numero == 1:
        return("Domingo.")
    if numero == 2:
        return("Segunda.")
    if numero == 3:
        return("Terça.")
    if numero == 4:
        return("Quarta.")
    if numero == 5:
        return("Quinta.")
    if numero == 6:
        return("Sexta.")
    if numero == 7:
        return("Sábado.")
    if numero > 7:
        return("")

# print(testa_dia_da_semana(1))
    
# exercício 3: calculadora simples
    
def soma(operacao, a, b):
    return (a + b)

def subtracao(operacao, a, b):
    return (a - b)

def multiplicacao(operacao, a ,b):
    return (a * b)

def divisao(operacao, a, b):
    return (a / b)

def calculadora():
    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))
    operacao = (input("Informe a operacão: "))
    if operacao == "soma":
        resultado = soma(operacao, a, b)
        print("Resultado: ", resultado)
    elif operacao == "subtração":
            resultado = subtracao(operacao, a, b)
            print("Resultado: ", resultado)
    elif operacao == "multiplicação":
        resultado = multiplicacao(operacao, a ,b)
        print("Resultado: ", resultado)
    elif operacao == "divisão":
        resultado = divisao(operacao, a, b)
        print("Resultado: ", resultado)
    else:
        print("Operação inválida.")

# calculadora()