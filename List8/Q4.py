import pandas as pd
df1 = pd.read_csv('https://www.dropbox.com/s/da1l9hbe8f0sgy8/fake-mercado19.csv?dl=1')
df2 = pd.read_csv('https://www.dropbox.com/s/iov7i28vpl4wqm9/fake-mercado04.csv?dl=1')
df3 = pd.read_csv('https://www.dropbox.com/s/i554mvb8b3ubpcx/fake-mercado20.csv?dl=1')
itens = []
for i in range(9):
    item = input(f"Digite o nome do item {i+1}: ")
    itens.append(item)
resultado = []
for item in itens:
    item1 = df1[df1['Item'] == item]
    item2 = df2[df2['Item'] == item]
    item3 = df3[df3['Item'] == item]
    valores = [(item1['Valor'].values[0], '1'), (item2['Valor'].values[0], '2'), (item3['Valor'].values[0], '3')]
    menor_valor, mercado = min(valores, key=lambda x: x[0])
    resultado.append([item1['Categoria'].values[0], item, menor_valor, mercado])
df_novo = pd.DataFrame(resultado, columns=['Categoria', 'Item', 'Menor Valor', 'Mercado'])
df_novo = df_novo.sort_values(by=['Categoria', 'Item'])
print(df_novo.to_string(index=False))
