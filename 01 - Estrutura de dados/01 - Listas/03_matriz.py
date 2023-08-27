# Acesso aos elementos de uma matriz (lista de listas) usando índices.

# Criação da matriz (lista de listas) com elementos diversos.
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Acesso à primeira lista (primeira linha) da matriz e impressão.
print(matriz[0])  # Resultado: [1, "a", 2]

# Acesso ao primeiro elemento da primeira lista (primeira linha) da matriz e impressão.
print(matriz[0][0])  # Resultado: 1

# Acesso ao último elemento da primeira lista (primeira linha) da matriz e impressão.
print(matriz[0][-1])  # Resultado: 2

# Acesso ao último elemento da última lista (última linha) da matriz e impressão.
print(matriz[-1][-1])  # Resultado: "c"

#     A matriz matriz é criada como uma lista de listas, representando uma matriz com três linhas e três colunas.

#     A linha print(matriz[0]) acessa e imprime a primeira lista (primeira linha) da matriz, resultando em [1, "a", 2].

#     A linha print(matriz[0][0]) acessa e imprime o primeiro elemento da primeira lista da matriz, resultando em 1.

#     A linha print(matriz[0][-1]) acessa e imprime o último elemento da primeira lista da matriz, resultando em 2.

#     A linha print(matriz[-1][-1]) acessa e imprime o último elemento da última lista (última linha) da matriz, resultando em "c".

# O código demonstra como acessar elementos específicos de uma matriz (lista de listas) usando índices e imprimir os valores correspondentes.
