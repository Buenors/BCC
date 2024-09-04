import pandas as pd
df=pd.read_csv("https://www.dropbox.com/s/aqo9magrsmob374/fake-classrooms11.csv?dl=1")
Média = df[input("Coluna a ser lida: ")].mean()
print("%.2f"% Média)