import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/i8lv141aanao5u3/fake-classrooms17.csv?dl=1")
coluna = input()
count_values = df[coluna].value_counts(sort=True, ascending=False)

count_values.name = "count"

output = f"{coluna}\n{count_values}"
print(output)