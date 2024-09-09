import pandas as pd

df = pd.read_csv("fake-classrooms15.csv")

coluna_lida1 = input()
coluna_lida2 = input()

media_coluna_lida1 = df[coluna_lida1].mean()
media_coluna_lida2 = df[coluna_lida2].mean()

print(f"Media {coluna_lida1} = {media_coluna_lida1:.2f}")
print(f"Media {coluna_lida2} = {media_coluna_lida2:.2f}")

if media_coluna_lida1 > 6.3 and media_coluna_lida2 > 6.3:
    print("As duas Medias sao maiores que 6.3")
elif media_coluna_lida1 > 6.3 and media_coluna_lida2 <= 6.3:
    print(f"Apenas Media {coluna_lida1} eh maior que 6.3")
elif media_coluna_lida2 > 6.3 and media_coluna_lida1 <= 6.3:
    print(f"Apenas Media {coluna_lida2} eh maior que 6.3")
else:
    print("Nenhuma das medias eh maior que 6.3")