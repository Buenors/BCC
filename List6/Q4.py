import pandas as pd

def calcula_distancia_manhattan(df, indice_p1, indice_p2, indice_p3):
    x1, y1 = df[['X', 'Y']].loc[indice_p1]
    x2, y2 = df[['X', 'Y']].loc[indice_p2]
    x3, y3 = df[['X', 'Y']].loc[indice_p3]

    distancia_p1_p2 = abs(x2 - x1) + abs(y2 - y1)
    distancia_p2_p3 = abs(x3 - x2) + abs(y3 - y2)
    distancia_p3_p1 = abs(x3 - x1) + abs(y3 - y1)

    soma_distancias = distancia_p1_p2 + distancia_p2_p3 + distancia_p3_p1

    return round(soma_distancias, 2)

def main():
    df = pd.read_csv("https://www.dropbox.com/s/s7dcmpu9kpqjgh0/pontos-plano-30.csv?dl=1")

    indice_p1 = int(input("Digite o índice do ponto 1: "))
    indice_p2 = int(input("Digite o índice do ponto 2: "))
    indice_p3 = int(input("Digite o índice do ponto 3: "))
   
    soma_distancias = calcula_distancia_manhattan(df, indice_p1, indice_p2, indice_p3)

    print(f"{soma_distancias}")

if __name__ == "__main__":
    main()