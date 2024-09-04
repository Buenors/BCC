import pandas as pd

def escreve_correlacao(df, nome_pais, x_col, y_col):
    df_pais = df[df['Pais'] == nome_pais]
    
    if x_col not in df_pais.columns or y_col not in df_pais.columns:
        print(f"Uma das colunas '{x_col}' ou '{y_col}' não existe no DataFrame.")
        return 
    
    correlacao = df_pais[x_col].corr(df_pais[y_col])

    print(f"{correlacao:.3f}")

def main():
    
    df = pd.read_csv("https://www.dropbox.com/s/zm235a2os1zexut/gapminder_full.csv?dl=1")
    nome_pais = input("Digite o nome do país: ")
    x_col = input("Digite o nome da coluna para o eixo X: ")
    y_col = input("Digite o nome da coluna para o eixo Y: ")

    escreve_correlacao(df, nome_pais, x_col, y_col)