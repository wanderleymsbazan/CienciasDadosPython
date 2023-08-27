# Acessando elementos de uma matriz (tupla de tuplas) usando índices.

# Matriz de elementos.
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Acessando a primeira linha da matriz (tupla) usando o índice 0.
print(matriz[0])  # Resultado: (1, "a", 2)

# Acessando o primeiro elemento da primeira linha usando índice duplo [linha][coluna].
print(matriz[0][0])  # Resultado: 1

# Acessando o último elemento da primeira linha usando índice duplo [linha][-1].
print(matriz[0][-1])  # Resultado: 2

# Acessando o último elemento da última linha usando índice duplo [-1][-1].
print(matriz[-1][-1])  # Resultado: "c"

#     A matriz matriz é criada como uma tupla de tuplas, representando uma matriz 3x3 com elementos diversos.

#     A linha print(matriz[0]) imprime a primeira linha da matriz, que é a tupla (1, "a", 2).

#     A linha print(matriz[0][0]) imprime o primeiro elemento da primeira linha, que é 1.

#     A linha print(matriz[0][-1]) imprime o último elemento da primeira linha, que é 2.

#     A linha print(matriz[-1][-1]) imprime o último elemento da última linha, que é "c".

# O código demonstra como acessar elementos específicos de uma matriz (tupla de tuplas) usando índices. Nesse caso, usamos um índice para selecionar a linha desejada e, em seguida, um segundo índice para selecionar o elemento dentro da linha.
