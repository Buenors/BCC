import pandas as pd
#Usando o comando pd.read_csv para conseguir ler a planilha e escolhendo df como a variável para armazená-la
df = pd.read_csv("fake-file10.csv")
#Salvo a planilha modificada como df_mod, e ordeno ela em meses e sálario em ordem decrescente
df_mod = df.sort_values(by=["Meses","Salario"], ascending=[False, False])
#Imprimo os 3 últimos valores da primeira linha usando o comando .values
#Para selecionar as 3 últimas colunas uso o -3:
print("Os 3 últimos valores da primeira linha são", df_mod.values[0][-3:])