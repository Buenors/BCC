import pandas as pd
#Usando o comando pd.read_csv para conseguir ler a planilha e escolhendo df como a variável para armazená-la
df = pd.read_csv("https://www.dropbox.com/s/cwfdaqzzznaetiz/fake-file02.csv?dl=1")
#Insiro o filtro desejado e obtenho a planilha filtrada
print(df.query("Salario >= 9383"))