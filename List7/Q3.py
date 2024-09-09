import pandas as pd
df = pd.read_csv(" https://www.dropbox.com/s/tkrs8wdr6y6oa4x/fake-classrooms27.csv?dl=1")

def calculaNota(linha):
    return (linha["Prova 1"] + linha["Prova 2"] + linha["Trabalho"]) / 3

def assign_concept(average, notaA, notaB, notaC, notaD):
    if average >= notaA:
        return 'A'
    elif average >= notaB:
        return 'B'
    elif average >= notaC:
        return 'C'
    elif average >= notaD:
        return 'D'
    else:
        return 'F'

notaA = input("Nota A: ")
notaB = input("Nota B: ")
notaC = input("Nota C: ")
notaD = input("Nota D: ")
notaA = float(notaA)
notaB = float(notaB)
notaC = float(notaC)
notaD = float(notaD)

df['Nota'] = df.apply(calculaNota, axis=1)

df['Conceito'] = df['Nota'].apply(lambda x: assign_concept(x, notaA, notaB, notaC, notaD))

def formataConceito(df):
    hist = df['Conceito'].value_counts()
    resp = ''
    if 'A' in hist.keys():
        resp += 'A: %d\n' % hist['A']
    if 'B' in hist.keys():
        resp += 'B: %d\n' % hist['B']
    if 'C' in hist.keys():
        resp += 'C: %d\n' % hist['C']
    if 'D' in hist.keys():
        resp += 'D: %d\n' % hist['D']
    if 'F' in hist.keys():
        resp += 'F: %d\n' % hist['F']
    return str(resp)

print(formataConceito(df))