C1 = float(input("Digite a temperatura em Celsius: "))               #Na entrada é preciso utilizar o comando float uma vez que a temperatura nem sempre será um numero inteiro\n",
C2 = float(input("Digite a segunda temperatura em Celsius "))         #Adotando as variáveis C1 e C2 como as temperaturas em Celsius e F1 e F2 como suas respectivas transformações\n",
F1 = (C1 * 9/5) + 32                                                 #Atribuído o valor de 54 para a variável C2\n",
F2 = (C2 * 9/5) + 32                                                 #A transformação da temperatura em Celsius (C) para Fahrenheit (F) se dá pela fórmula (C * 9/5) / 32\n",
print("As temperaturas em Fahrenheit são %.2f e %.2f" % (F1, F2))    #A saída com apenas duas casas decimais"