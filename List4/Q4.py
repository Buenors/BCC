import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/5cdx81qegek9auj/fake-classrooms19.csv?dl=1")
DP = df[input("Coluna a ser lida: ")].std()
print("%.2f" % DP)