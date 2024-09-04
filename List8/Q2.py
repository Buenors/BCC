import pandas as pd
df = pd.read_csv('https://www.dropbox.com/s/fzoqpkubhweth7f/fake-mercado15.csv?dl=1')
itens_comprados = []
for i in range(9):
  item = input().strip()
  itens_comprados.append(item)
novo = []
total_gasto = 0
for item in itens_comprados:
    item_data = df[df['Item'] == item]
    if not item_data.empty:
        valor = item_data['Valor'].values[0]
        quantidade_disponivel = item_data['Quantidade'].values[0]
        quantidade_comprada = min(quantidade_disponivel, 5)
        subtotal = valor * quantidade_comprada
        total_gasto += subtotal
        categoria = item_data['Categoria'].values[0]
        novo.append([categoria, item, valor, quantidade_comprada, subtotal])

df_novo = pd.DataFrame(novo, columns=['Categoria', 'Item', 'Valor', 'Quantidade', 'Subtotal']).sort_values(by=['Categoria', 'Item'], ascending=[True, True])
print(df_novo.to_string(index=False))