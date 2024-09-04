import pandas as pd
df = pd.read_csv(" https://www.dropbox.com/s/5dwp17fjk7m3nf4/fake-classrooms08.csv?dl=1")
Moda = df[input("Coluna a ser lida: ")].mode()
print("%.2f"% Moda)