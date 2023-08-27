# Demonstração de slicing em uma lista.

# Criação da lista de caracteres.
lista = ["p", "y", "t", "h", "o", "n"]

# Faz slicing da lista a partir do índice 2 até o final.
print(lista[2:])  # Resultado: ["t", "h", "o", "n"]

# Faz slicing da lista do início até o índice 2 (exclusivo).
print(lista[:2])  # Resultado: ["p", "y"]

# Faz slicing da lista do índice 1 até o índice 3 (exclusivo).
print(lista[1:3])  # Resultado: ["y", "t"]

# Faz slicing da lista do índice 0 até o índice 3 (exclusivo), pulando de 2 em 2.
print(lista[0:3:2])  # Resultado: ["p", "t"]

# Faz slicing da lista completa (cópia da lista original).
print(lista[:])  # Resultado: ["p", "y", "t", "h", "o", "n"]

# Faz slicing da lista completa em ordem reversa.
print(lista[::-1])  # Resultado: ["n", "o", "h", "t", "y", "p"]

#     A lista lista é criada com os caracteres "p", "y", "t", "h", "o" e "n".

#     A linha print(lista[2:]) faz slicing da lista a partir do índice 2 até o final, resultando em ["t", "h", "o", "n"].

#     A linha print(lista[:2]) faz slicing da lista do início até o índice 2 (exclusivo), resultando em ["p", "y"].

#     A linha print(lista[1:3]) faz slicing da lista do índice 1 até o índice 3 (exclusivo), resultando em ["y", "t"].

#     A linha print(lista[0:3:2]) faz slicing da lista do índice 0 até o índice 3 (exclusivo), pulando de 2 em 2, resultando em ["p", "t"].

#     A linha print(lista[:]) faz slicing da lista completa, resultando em uma cópia da lista original.

#     A linha print(lista[::-1]) faz slicing da lista completa em ordem reversa, resultando em ["n", "o", "h", "t", "y", "p"].

# O código demonstra como fazer slicing em uma lista em Python, permitindo a extração de partes específicas da lista usando índices e passos.