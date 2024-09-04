import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/tcbxw0s0edp3ghm/fake-mercado14.csv?dl=1')
categoria = input()
filtro = (df['Categoria'] == categoria) & (df['Quantidade'] <= 3)
produtos_filtrados = df[filtro]
total_gasto = 0
print("Item; Valor; Quantidade; Gasto")
for index, row in produtos_filtrados.iterrows():
    item = row['Item']
    valor = row['Valor']
    quantidade = row['Quantidade']
    gasto = (11 - quantidade) * valor
    total_gasto += gasto
    print(f"{item}; {'%s '% valor}; {quantidade}; {gasto:.2f}")
print(f"Total gasto para repor os estoques: {total_gasto:.2f}")