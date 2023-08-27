# Diferença de conjuntos usando o método difference().

# Dois conjuntos iniciais.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Usando o método difference() para encontrar a diferença entre conjunto_a e conjunto_b.
resultado = conjunto_a.difference(conjunto_b)

# Exibindo o resultado da diferença.
print(resultado)  # Resultado: {1}

# Usando o método difference() para encontrar a diferença entre conjunto_b e conjunto_a.
resultado = conjunto_b.difference(conjunto_a)

# Exibindo o resultado da diferença.
print(resultado)  # Resultado: {4}

#     Você começa definindo dois conjuntos conjunto_a e conjunto_b, que contêm os elementos 1, 2, 3 e 2, 3, 4, respectivamente.

#     O método difference() é usado para encontrar a diferença entre os conjuntos. Quando você chama conjunto_a.difference(conjunto_b), ele retorna um novo conjunto contendo os elementos que estão presentes em conjunto_a mas não em conjunto_b. Da mesma forma, conjunto_b.difference(conjunto_a) retorna um conjunto contendo os elementos que estão presentes em conjunto_b mas não em conjunto_a.

#     Os resultados das diferenças são armazenados na variável resultado.

#     Os print(resultado) exibem os conjuntos resultantes, que contêm os elementos {1} e {4}, respectivamente.

# O método difference() é útil para encontrar os elementos que estão em um conjunto, mas não no outro.