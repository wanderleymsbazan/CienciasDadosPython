# Demonstração de fatiamento (slicing) em uma tupla.

# Tupla de letras.
tupla = ("p", "y", "t", "h", "o", "n",)

# Fatiando a tupla a partir do índice 2 até o final.
print(tupla[2:])  # Resultado: ("t", "h", "o", "n")

# Fatiando a tupla do início até o índice 2 (não inclusivo).
print(tupla[:2])  # Resultado: ("p", "y")

# Fatiando a tupla do índice 1 até o índice 3 (não inclusivo).
print(tupla[1:3])  # Resultado: ("y", "t")

# Fatiando a tupla do índice 0 até o índice 3 com passo 2.
print(tupla[0:3:2])  # Resultado: ("p", "t")

# Fatiando a tupla completa (equivalente à tupla original).
print(tupla[::])  # Resultado: ("p", "y", "t", "h", "o", "n")

# Fatiando a tupla em ordem inversa usando passo negativo.
print(tupla[::-1])  # Resultado: ("n", "o", "h", "t", "y", "p")

#     A tupla tupla contém os elementos "p", "y", "t", "h", "o" e "n".

#     tupla[2:] retorna uma nova tupla que começa no índice 2 até o final da tupla.

#     tupla[:2] retorna uma nova tupla que começa no início da tupla e vai até o índice 2 (não inclusivo).

#     tupla[1:3] retorna uma nova tupla que começa no índice 1 e vai até o índice 3 (não inclusivo).

#     tupla[0:3:2] retorna uma nova tupla que começa no índice 0, vai até o índice 3 (não inclusivo) e pula de 2 em 2.

#     tupla[::] retorna uma cópia da tupla completa, o que é equivalente à própria tupla.

#     tupla[::-1] retorna uma nova tupla que é uma reversão da tupla original, usando um passo negativo para percorrer a tupla de trás para frente.

# O código demonstra diferentes formas de fatiar uma tupla em Python para obter subconjuntos específicos de elementos.