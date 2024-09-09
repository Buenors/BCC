#Adotando as variáveis das idades em anos para Maria e João como, respectivamente, X e Y
Y = int(input("Insira a idade de João "))
#Atribuído o valor de 20 para a variável X
X = int(input("Insira a idade de Maria "))
#Para sabermos a idade deles em segundos devemos multiplicar as variáveis X e Y por 365(dias)*24(horas)*3600(segundos)
#E adotando S como o tempo em segundos para cada 1 ano de vida
S = 365*86400
#Adotando as variáveis das idades em segundos para Maria e João como, respectivamente, M e J
M = X * S
J = Y * S
#Saida com apenas os números, de Maria e João respectivamente
print(M, J)