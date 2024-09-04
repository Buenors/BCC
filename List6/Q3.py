import pandas as pd

def calcula_distancia_manhattan(df, indice_p1, indice_p2):
    x1, y1 = df[['X', 'Y']].loc[indice_p1]
    x2, y2 = df[['X', 'Y']].loc[indice_p2]
    
    distancia = abs(x2 - x1) + abs(y2 - y1)
    
    return round(distancia, 2)

def main():
    df = pd.read_csv("https://www.dropbox.com/s/biwb2cseymnxdpb/pontos-plano-29.csv?dl=1")
    
    indice_p1 = int(input("Digite o índice do ponto 1: "))
    indice_p2 = int(input("Digite o índice do ponto 2: "))
    
    distancia = calcula_distancia_manhattan(df, indice_p1, indice_p2)
    print(f"{distancia:.2f}")

if __name__ == "__main__":
    main()