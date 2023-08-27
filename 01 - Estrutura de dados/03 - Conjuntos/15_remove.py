# Manipulando um conjunto usando o método remove().

# Inicializando um conjunto chamado "numeros".
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Exibindo o conjunto original.
print(numeros)  # Resultado: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Usando o método remove() para remover um elemento específico do conjunto.
# O método remove() retorna None, não o elemento removido.
numeros.remove(0)
print(numeros)  # Resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9}

#     O conjunto "numeros" é inicializado com vários elementos, incluindo duplicatas.

#     O método remove() é usado para remover um elemento específico do conjunto. Nesse caso, o elemento 0 é removido do conjunto.

#     O método remove() não retorna o elemento removido, ele retorna None. Por isso, não é possível fazer print(numeros.remove(0)) para exibir o elemento removido.

#     Após a remoção, o conjunto "numeros" é exibido novamente, mostrando os elementos restantes.

# Lembre-se de que o método remove() remove um elemento específico do conjunto. Se o elemento não estiver presente no conjunto, isso resultará em um erro KeyError. Certifique-se de que o elemento que você está tentando remover esteja realmente no conjunto antes de usar o método remove().