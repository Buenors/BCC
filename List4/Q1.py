import pandas as pd
df=pd.read_csv("https://www.dropbox.com/s/14v1j6gzqcgod8o/fake-classrooms15.csv?dl=1")
Var = df[input("Escolha uma coluna da tabela: ")].var()
print("%.2f" % Var)