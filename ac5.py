import random

def main():
    vida = 100
    ataque = random.randint(10, 20)
    defesa = random.randint(1, 5)
    print("Aventureiro: vida", vida, " - ",  "ataque", ataque, " - ","defesa", defesa,)
    vida2 = random.randint(60, 80)
    ataque2 = random.randint(20, 30)
    print("Monstro: vida", vida2, " - ",  "ataque", ataque2)
    rodada_num = 1
    while vida > 0 and vida2 > 0:
        print("Rodada", rodada_num)
        rodada_num = rodada_num + 1
        danoA = random.randint(1, ataque)
        danoM = random.randint(1, ataque2)
        vida = (vida - (danoM - defesa))
        vida2 = (vida2 - danoA )
        print("Aventureiro: vida", vida, " - ",  "ataque", ataque, " - ","defesa", defesa,)
        print("Monstro: vida", vida2, " - ",  "ataque", ataque2)
        if vida < 0:
            print("Aventureiro morreu.")
            break
        if vida2 < 0:
            print("Monstro morreu.")
            break

main()









