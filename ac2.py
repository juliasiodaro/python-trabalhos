""" Julia Siodaro Engenharia de Software tarde
AC 2

"""
# revisitando a AC 1 exercicio 1

# ** 0,5

def bhaskara_menos(a, b, c):
    return(- b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

def bhaskara_mais(a, b, c):
    return(- b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

def valores():
    a = float(input("Informe o parâmetro a da equação: "))
    b = float(input("Informe o parâmetro b da equação: "))
    c = float(input("Informe o parâmetro c da equação: "))
    print("A primeira raiz da equação é", bhaskara_menos(a, b, c))
    print("A segunda raiz da equação é", bhaskara_mais(a, b, c))  
      
valores() 

# exercicio 2

def e_bi(ano):
    bissexto = False
    if ano%4 == 0 and ano%100 != 0:
        bissexto = True
    elif ano%400 == 0:
        bissexto = True
    return bissexto

def ano():
   ano = int(input("Informe o ano: "))
   print("O ano é bissexto: ", e_bi(ano))

ano()

# AC 2 --------------------------------------------------------------------------------------

def calcular_salario(valor_hora, num_hora):
    return(valor_hora * num_hora) - (valor_hora * num_hora * 0.275)

def infos():
    valor_hora = float(input("Informe o valor por hora: "))
    num_hora = float(input("Informe o número de horas: "))
    print("O salário líquido é de:", calcular_salario(valor_hora, num_hora))

infos()
