import pandas as pd
#Usando o comando pd.read_csv para conseguir ler a planilha e escolhendo df como a variável para armazená-la
df = pd.read_csv("https://www.dropbox.com/s/fklekauxy0n3xdy/fake-file06.csv?dl=1")
#faço os filtros desejados e por fim junto os dois obtendo o planilha filtrada
filtro1 = "Funcionario > 10"
filtro2 = "Meses <= 47"
filtros = filtro1 + " and " + filtro2
print(df.query(filtros))