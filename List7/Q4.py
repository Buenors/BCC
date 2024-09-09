import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("https://www.dropbox.com/s/6bif4nwgy1n6ope/fake-classrooms15.csv?dl=1")

# Função para calcular o conceito com base na média
def calcular_conceito(media):
    if media >= 8.3:
        return 'A'
    elif media >= 7.0:
        return 'B'
    elif media >= 6.0:
        return 'C'
    elif media >= 4.9:
        return 'D'
    else:
        return 'F'

# Simulação da entrada do usuário
indice_aluno = int(input("Indice: "))  # Exemplo: o usuário inseriu o índice 1

# Selecionando as informações do aluno pelo índice
nome, prova1, prova2, trabalho = df[["Nome", "Prova 1", "Prova 2", "Trabalho"]].loc[indice_aluno]

# Calculando a média
media = (prova1 + prova2 + trabalho) / 3

# Obtendo o conceito final
conceito = calcular_conceito(media)

# Formatando a saída
print(f"Nome: {nome}\n"
      f"Prova 1: {prova1:.1f}\n"
      f"Prova 2: {prova2:.1f}\n"
      f"Trabalho: {trabalho:.1f}\n"
      f"Media: {media:.2f}\n"
      f"Conceito: {conceito}")
