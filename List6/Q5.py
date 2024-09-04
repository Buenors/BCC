import pandas as pd
import math
def distancia_terra(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Fórmula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  
    distancia = r * c
    return distancia

def calcula_distancia_km(df, indice_city1, indice_city2):
    latitude1, longitude1 = df[["latitude", "longitude"]].loc[indice_city1]
    latitude2, longitude2 = df[["latitude", "longitude"]].loc[indice_city2]
    distancia = distancia_terra(latitude1, longitude1, latitude2, longitude2)
    return round(distancia, 2)

def main():
    df = pd.read_csv("https://www.dropbox.com/s/8tq1bxi8acps36p/latitude-longitude-bairros.csv?dl=1")
    indice_city1 = int(input("Digite o índice da primeira cidade: "))
    indice_city2 = int(input("Digite o índice da segunda cidade: "))
    
    distancia = calcula_distancia_km(df, indice_city1, indice_city2)
    
    print(f"{distancia}")

if __name__ == "__main__":
    main()