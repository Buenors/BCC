import pandas as pd
#Usando o comando pd.read_csv para conseguir ler a planilha e escolhendo df como a variável para armazená-la
df = pd.read_csv("fake-file08.csv")
#Para mostrar o valor da célula que está na linha 7 e na coluna 1 utilizo o comando df.values
print(df.values[7][1])