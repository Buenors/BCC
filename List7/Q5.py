import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("https://www.dropbox.com/s/yctp3kyb5worjvc/fake-classrooms21.csv?dl=1")

# Função para calcular o conceito com base na média
def calcular_conceito(media):
    if media >= 6.3:
        return 'Aprovado'
    else:
        return 'Reprovado'

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