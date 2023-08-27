# Verificação de subconjunto usando o método issubset().

# Dois conjuntos iniciais.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Usando o método issubset() para verificar se conjunto_a é subconjunto de conjunto_b.
resultado = conjunto_a.issubset(conjunto_b)  # True

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: True

# Usando o método issubset() para verificar se conjunto_b é subconjunto de conjunto_a.
resultado = conjunto_b.issubset(conjunto_a)  # False

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: False

#     Você começa definindo dois conjuntos conjunto_a e conjunto_b, que contêm os elementos 1, 2, 3 e 4, 1, 2, 5, 6, 3, respectivamente.

#     O método issubset() é usado para verificar se um conjunto é um subconjunto de outro conjunto. Quando você chama conjunto_a.issubset(conjunto_b), ele retorna True se todos os elementos de conjunto_a estiverem presentes em conjunto_b. Da mesma forma, conjunto_b.issubset(conjunto_a) retorna True se todos os elementos de conjunto_b estiverem presentes em conjunto_a.

#     Os resultados das verificações são armazenados na variável resultado.

#     Os print(resultado) exibem os resultados das verificações, que são True e False, respectivamente.

# O método issubset() é usado para determinar se um conjunto é um subconjunto de outro, ou seja, se todos os elementos do primeiro conjunto estão presentes no segundo conjunto.
