import pandas as pd

df = pd.read_csv('https://www.dropbox.com/s/fe01qd4i2cgyjvr/fake-classrooms-correl18.csv?dl=1')

coluna_para_normalizar = input()

df['Nota Final'] = df['Nota Final'] / df['Nota Final'].max()
df[f'{coluna_para_normalizar}'] = df[coluna_para_normalizar] / df[coluna_para_normalizar].max()

print(df[['Nota Final', f'{coluna_para_normalizar}']].head())
