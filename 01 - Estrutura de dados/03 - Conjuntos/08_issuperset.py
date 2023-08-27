# Verificação de superconjunto usando o método issuperset().

# Dois conjuntos iniciais.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Usando o método issuperset() para verificar se conjunto_a é superconjunto de conjunto_b.
resultado = conjunto_a.issuperset(conjunto_b)  # False

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: False

# Usando o método issuperset() para verificar se conjunto_b é superconjunto de conjunto_a.
resultado = conjunto_b.issuperset(conjunto_a)  # True

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: True

#     Você começa definindo dois conjuntos conjunto_a e conjunto_b, que contêm os elementos 1, 2, 3 e 4, 1, 2, 5, 6, 3, respectivamente.

#     O método issuperset() é usado para verificar se um conjunto é um superconjunto de outro conjunto. Quando você chama conjunto_a.issuperset(conjunto_b), ele retorna True se todos os elementos de conjunto_b estiverem presentes em conjunto_a. Da mesma forma, conjunto_b.issuperset(conjunto_a) retorna True se todos os elementos de conjunto_a estiverem presentes em conjunto_b.

#     Os resultados das verificações são armazenados na variável resultado.

#     Os print(resultado) exibem os resultados das verificações, que são False e True, respectivamente.

# O método issuperset() é usado para determinar se um conjunto é um superconjunto de outro, ou seja, se contém todos os elementos do segundo conjunto.
