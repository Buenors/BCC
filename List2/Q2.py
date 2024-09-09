import pandas as pd
#Usando o comando pd.read_csv para conseguir ler a planilha e escolhendo df como a variável para armazená-la
df = pd.read_csv("fake-file10.csv")
#Escolhendo colst1 como a variável para armazenar a coluna idade
colst1 = 'Idade'
#E assim utilizando o comando .mean para obter a média das idades
print("O resultado do operador médio das idades é", df[colst1].values.mean())