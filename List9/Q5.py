import pandas as pd
import numpy as np

coluna = input("Digite o nome da coluna: ")

df = pd.read_csv("https://www.dropbox.com/s/ztgwtiwucvkj8wx/simulacao1000.csv?dl=1")

media = df[coluna].mean()
desvio_padrao = df[coluna].std()
correlacao = df['Ncirc'].corr(df[coluna])

print(f"Coluna = {coluna}")
print(f"Media = {media:.6f}")
print(f"Desvio padrao = {desvio_padrao:.6f}")
print(f"Correlacao = {correlacao:.6f}")