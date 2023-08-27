# Diferença simétrica de conjuntos usando o método symmetric_difference().

# Dois conjuntos iniciais.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Usando o método symmetric_difference() para encontrar a diferença simétrica entre conjunto_a e conjunto_b.
resultado = conjunto_a.symmetric_difference(conjunto_b)

# Exibindo o resultado da diferença simétrica.
print(resultado)  # Resultado: {1, 4}

#     Você começa definindo dois conjuntos conjunto_a e conjunto_b, que contêm os elementos 1, 2, 3 e 2, 3, 4, respectivamente.

#     O método symmetric_difference() é usado para encontrar a diferença simétrica entre os conjuntos. Ele retorna um novo conjunto contendo os elementos que estão presentes em um dos conjuntos, mas não em ambos.

#     O resultado da diferença simétrica é armazenado na variável resultado.

#     O print(resultado) exibe o conjunto resultante, que contém os elementos {1, 4}, que são os elementos presentes em apenas um dos conjuntos.

# O método symmetric_difference() é útil para encontrar os elementos que estão em um dos conjuntos, mas não em ambos.