# Remoção de elementos de um conjunto usando o método discard().

# Inicializando um conjunto chamado "numeros".
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Exibindo o conjunto antes da remoção.
print(numeros)  # Resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# Usando o método discard() para remover o elemento 1 (se presente).
numeros.discard(1)

# Usando o método discard() para remover o elemento 45 (não presente no conjunto).
numeros.discard(45)

# Exibindo o conjunto após as remoções.
print(numeros)  # Resultado: {2, 3, 4, 5, 6, 7, 8, 9, 0}

#     Você começa inicializando um conjunto chamado "numeros" com vários elementos, incluindo duplicatas.

#     O método discard(elemento) é usado para remover um elemento do conjunto, caso ele esteja presente. Se o elemento não estiver presente no conjunto, a operação não terá efeito.

#     Você chama numeros.discard(1) para remover o elemento 1 do conjunto, se estiver presente. Como o elemento 1 está presente, ele é removido.

#     Você chama numeros.discard(45) para remover o elemento 45 do conjunto. Como o elemento 45 não está presente, essa operação não tem efeito.

#     O conjunto "numeros" é exibido após as remoções, mostrando os elementos restantes.

# O método discard() é útil para remover elementos de um conjunto sem gerar erros caso o elemento não esteja presente.