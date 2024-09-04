import pandas as pd
import math

def calcula_esfera_area(df, indice_p):
    x, y, z = df[['X', 'Y', 'Z']].loc[indice_p]
 
    r = math.sqrt(x**2 + y**2 + z**2)

    area = 4 * math.pi * r**2

    return round(area, 2)

def main():
    df = pd.read_csv("https://www.dropbox.com/s/biwb2cseymnxdpb/pontos-plano-29.csv?dl=1")

    indice_p = int(input("Digite o índice do ponto: "))

    area = calcula_esfera_area(df, indice_p)

    print(f"{area}")

if __name__ == "__main__":
    main()