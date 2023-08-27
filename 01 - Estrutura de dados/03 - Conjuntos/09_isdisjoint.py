# Verificação de conjuntos disjuntos usando o método isdisjoint().

# Três conjuntos iniciais.
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# Usando o método isdisjoint() para verificar se conjunto_a e conjunto_b são disjuntos.
resultado = conjunto_a.isdisjoint(conjunto_b)  # True

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: True

# Usando o método isdisjoint() para verificar se conjunto_a e conjunto_c são disjuntos.
resultado = conjunto_a.isdisjoint(conjunto_c)  # False

# Exibindo o resultado da verificação.
print(resultado)  # Resultado: False

#     Você começa definindo três conjuntos: conjunto_a, conjunto_b e conjunto_c, que contêm os elementos 1, 2, 3, 4, 5, 6, 7, 8, 9 e 1, 0, respectivamente.

#     O método isdisjoint() é usado para verificar se dois conjuntos são disjuntos, ou seja, se eles não têm elementos em comum. Quando você chama conjunto_a.isdisjoint(conjunto_b), ele retorna True se não houver nenhum elemento comum entre conjunto_a e conjunto_b. Da mesma forma, conjunto_a.isdisjoint(conjunto_c) retorna False, pois os conjuntos têm o elemento 1 em comum.

#     Os resultados das verificações são armazenados na variável resultado.

#     Os print(resultado) exibem os resultados das verificações, que são True e False, respectivamente.

# O método isdisjoint() é usado para determinar se dois conjuntos não têm elementos em comum.