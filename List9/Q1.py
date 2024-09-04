import random as rd

numeroaposta = int(input("número apostado "))
saldo = int(input("saldo disponível "))
aposta = int(input("valor da aposta "))
rd.seed(1)
perdeu = 0
ganhou = 0
while saldo > 0 and saldo < 620:
    sorteio = rd.randint(1,2)
    if sorteio == numeroaposta:
        saldo = saldo+aposta
        ganhou = ganhou + 1
    else: 
        saldo = saldo-aposta
        perdeu = perdeu+1

print(f"O jogador perdeu {perdeu} vezes e lucrou {ganhou}  vezes")
print(f"O jogador tem {saldo} reais")