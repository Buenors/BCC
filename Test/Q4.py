import random

def main():
    semente = int(input("Insira o valor da seed: "))

    random.seed(semente)

    # Inicializa contadores de caras para os jogadores
    jogador1_caras = 0
    jogador2_caras = 0

    # Número de jogadas
    num_jogadas = 12

    # Simulação das jogadas
    for _ in range(num_jogadas):
        # Sorteia os números para cada jogador
        resultado_jogador1 = random.randint(9, 10)
        resultado_jogador2 = random.randint(9, 10)

        # Conta os números 9 (cara)
        if resultado_jogador1 == 9:
            jogador1_caras += 1
        if resultado_jogador2 == 9:
            jogador2_caras += 1

    # Determina o vencedor
    if jogador1_caras > jogador2_caras:
        vencedor = "Jogador 1"
    elif jogador2_caras > jogador1_caras:
        vencedor = "Jogador 2"
    else:
        vencedor = "Empate"

    # Imprime os resultados
    print(f"Número de jogadas: {num_jogadas}")
    print(f"Jogador 1: {jogador1_caras} caras")
    print(f"Jogador 2: {jogador2_caras} caras")
    print(f"{vencedor} ganhou!")

if __name__ == "__main__":
    main()