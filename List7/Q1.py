import pandas as pd
df = pd.read_csv("fake-classrooms17.csv")
def get_student_result(indice_aluno):
    student = df.loc[indice_aluno, ["Nome", "Prova 1", "Prova 2", "Trabalho"]]
    media = (student["Prova 1"] * 0.25) + (student["Prova 2"] * 0.60) + (student["Trabalho"] * 0.15)
    result = "Aprovado" if media >= 5.1 else "Reprovado"
    print("Nome:", student["Nome"])
    print("Prova 1:", student["Prova 1"])
    print("Prova 2:", student["Prova 2"])
    print("Trabalho:", student["Trabalho"])
    print(f"Média: {media:.2f}")
    print("Resultado:", result)