import random as rd

numeroaposta = int(input("Número apostado "))
saldo = int(input("Saldo disponível "))
aposta = int(input("Valor da aposta "))
simulation = int(input("Simulações "))
rd.seed(int(input("Valor da seed ")))
faliu = 0
prosp = 0
for i in range(0,simulation):
    sorteio = rd.randint(1,2)
    if sorteio == numeroaposta:
        saldo += aposta
        if saldo >= 240:
            prosp += 1
    else: 
        saldo = saldo-aposta
        if saldo < 240:
            faliu += 1
if faliu > prosp :
    maiormenor = "maior que"
if faliu < prosp :
    maiormenor = "menor que"
if faliu == prosp :
    maiormenor = "igual" 
print(f"O jogador prosperou {prosp} vezes\nO jogador faliu {faliu} vezes\nNumero de vezes que o jogador faliu eh {maiormenor} o numero de vezes que prosperou")
