import random as rd

rd.seed(input("Valor da seed "))
num_jogadas = 12
jogador1_caras = 0
jogador2_caras = 0

# Simulando as jogadas
for _ in range(num_jogadas):
    resultado_jogador1 = rd.randint(3, 4)
    resultado_jogador2 = rd.randint(3, 4)

    if resultado_jogador1 == 3:
        jogador1_caras += 1
    if resultado_jogador2 == 3:
        jogador2_caras += 1

if jogador2_caras >= jogador1_caras :
    campeao = "Jogador 2"
else:
    campeao = "Jogador 1"

print(f"Número de jogadas: {num_jogadas}\nJogador 1: {jogador1_caras}  caras \nJogador 2: {jogador2_caras} caras\n{campeao} ganhou!")
