# Manipulando um conjunto usando o método pop().

# Inicializando um conjunto chamado "numeros".
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Exibindo o conjunto original.
print(numeros)  # Resultado: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Usando o método pop() para remover e retornar um elemento do conjunto.
# O elemento removido é arbitrário, pois conjuntos não têm ordem definida.
elemento_removido = numeros.pop()
print(elemento_removido)  # Resultado: Um dos elementos removidos, por exemplo, 0

elemento_removido = numeros.pop()
print(elemento_removido)  # Resultado: Outro elemento removido, por exemplo, 1

# Exibindo o conjunto após a remoção dos elementos.
print(numeros)  # Resultado: Os elementos restantes no conjunto.

#     O conjunto "numeros" é inicializado com vários elementos, incluindo duplicatas.

#     O método pop() é usado para remover e retornar um elemento do conjunto. Como os conjuntos não têm uma ordem definida, o elemento removido é arbitrário.

#     Você chama numeros.pop() duas vezes, o que remove e retorna elementos do conjunto. A ordem em que os elementos são removidos é arbitrária devido à natureza dos conjuntos.

#     Após as remoções, o conjunto "numeros" é exibido novamente, mostrando os elementos restantes.

# Lembre-se de que, devido à natureza dos conjuntos, a ordem em que os elementos são removidos usando pop() pode variar, e os elementos são removidos arbitrariamente.