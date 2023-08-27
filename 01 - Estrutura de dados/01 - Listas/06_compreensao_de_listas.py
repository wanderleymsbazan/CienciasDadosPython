# Demonstração de filtragem e modificação de lista usando list comprehension.

# Lista de números.
numeros = [1, 30, 21, 2, 9, 65, 34]

# List comprehension para filtrar os números pares da lista.
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # Resultado: [30, 2, 34]

# List comprehension para calcular o quadrado de cada número na lista.
quadrado = [numero**2 for numero in numeros]
print(quadrado)  # Resultado: [1, 900, 441, 4, 81, 4225, 1156]

#     A lista numeros contém sete números inteiros.

#     A linha pares = [numero for numero in numeros if numero % 2 == 0] utiliza list comprehension para criar uma nova lista pares contendo os números pares da lista numeros.

#     A linha print(pares) imprime a lista pares, que contém os números pares [30, 2, 34].

#     A linha quadrado = [numero**2 for numero in numeros] utiliza list comprehension para criar uma nova lista quadrado contendo o quadrado de cada número na lista numeros.

#     A linha print(quadrado) imprime a lista quadrado, que contém o quadrado de cada número [1, 900, 441, 4, 81, 4225, 1156].

# O código demonstra como usar list comprehension para filtrar e modificar elementos em uma lista de maneira concisa e eficiente.