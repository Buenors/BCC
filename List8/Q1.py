import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/6ovye11b21lyrcu/fake-mercado16.csv?dl=1')
itens_comprados = []
for i in range(12):
    item = input().strip()
    itens_comprados.append(item)
total_gasto = 0
print("Item; Valor; Quantidade; Subtotal")
for item in itens_comprados:
    item_data = df[df['Item'] == item]
    if not item_data.empty:
        valor = item_data['Valor'].values[0]
        quantidade_disponivel = item_data['Quantidade'].values[0]
        quantidade_comprada = min(quantidade_disponivel, 2)
        subtotal = valor * quantidade_comprada
        total_gasto += subtotal
        print(f"{item}; {valor}; {quantidade_comprada}; {subtotal:.2f}")
print(f"Total gasto na compra: {total_gasto:.2f}")