import random

semente = int(input("Digite a semente: "))
num_caixas = int(input("Digite o número total de caixas: "))

random.seed(semente)

pesos = [1, 2, 3]
probabilidades = [0.4, 0.4, 0.2]

caixas = random.choices(pesos, weights=probabilidades, k=num_caixas)

contador = [0] * len(pesos)
for caixa in caixas:
    contador[caixa - 1] += 1

probabilidades_observadas = [count / num_caixas for count in contador]

for i, probabilidade in enumerate(probabilidades_observadas):
    print(f"Probabilidade de ocorrência da caixa {pesos[i]} = {probabilidade:.4f}")