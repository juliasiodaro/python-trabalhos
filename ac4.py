""" 
Julia Siodaro AC 4 Engenharia de Software tarde

"""

def ler_nome_usuario():
    return input("Informe o seu nome: ")

def ler_notas():
    ap1 = float(input("Informe o valor de ap1: "))
    ap2 = float(input("Informe o valor de ap2: "))
    as1 = float(input("Informe o valor de as: "))
    ac = float(input("Informe o valor de ac: "))
    return ap1, ap2, as1, ac

def validar_notas(ap1, ap2, as1, ac):
    if ap1 < 0 or ap1 > 10:
        return False
    if ap2 < 0 or ap2 > 10:
        return False
    if as1 < 0 or as1 > 10:
        return False
    if ac < 0 or ac > 10:
        return False
    return True

def duas_maiores(ap1, ap2, as1):
    if as1 > ap1:
        return as1, ap2
    if as1 > ap2:
        return as1, ap1
    return ap1, ap2



def calcular_media(n1, n2, ac):
    return float(n1 + n2) * 0.4 + ac * 0.2



def informar_aprov(media):
    if media >= 7:
        print("Parabéns. Você foi Aprovado.")
    if media < 7:
        print("Você foi reprovado.")


def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, as1, ac = ler_notas()
        if validar_notas(ap1, ap2, as1, ac):
            n1, n2 = duas_maiores(ap1, ap2, as1)
            media = calcular_media(n1, n2, ac)
            print("Sua média é:", calcular_media(n1, n2, ac))
            informar_aprov(media)

main()