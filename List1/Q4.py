a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))
#Importar a biblioteca math pra usar a funçao .sqrt
import math
delta = b**2 - 4*a*c
#Assumindo que delta será sempre maior que zero teremos sempre duas raízes distintas
raiz1 = (-b + math.sqrt(delta))/(2*a)
raiz2 = (-b - math.sqrt(delta))/(2*a)
print("As raízes são ""%.2f e %.2f"% (raiz1, raiz2))