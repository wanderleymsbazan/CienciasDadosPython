# Adição de elementos a um conjunto usando o método add().

# Inicializando um conjunto chamado "sorteio".
sorteio = {1, 23}

# Usando o método add() para adicionar o número 25 ao conjunto "sorteio".
sorteio.add(25)  # {1, 23, 25}

# Exibindo o conjunto após a adição.
print(sorteio)  # Resultado: {1, 23, 25}

# Usando o método add() para adicionar o número 42 ao conjunto "sorteio".
sorteio.add(42)  # {1, 23, 25, 42}

# Exibindo o conjunto após a adição.
print(sorteio)  # Resultado: {1, 23, 25, 42}

# Tentando adicionar o número 25 novamente ao conjunto "sorteio".
# Como o número 25 já está presente no conjunto, esta operação não afetará o conjunto.
sorteio.add(25)  # {1, 23, 25, 42}

# Exibindo o conjunto após a tentativa de adição.
print(sorteio)  # Resultado: {1, 23, 25, 42}

#     Você começa inicializando um conjunto chamado "sorteio" com os elementos 1 e 23.

#     O método add() é usado para adicionar elementos a um conjunto. Quando você chama sorteio.add(25), o número 25 é adicionado ao conjunto "sorteio". O mesmo acontece quando você chama sorteio.add(42).

#     No terceiro uso do método add(), você está tentando adicionar o número 25 novamente ao conjunto. No entanto, como o número 25 já está presente no conjunto, essa operação não tem efeito.

#     Os print(sorteio) exibem o conjunto após cada adição ou tentativa de adição, mostrando os elementos presentes no conjunto.

# O método add() é usado para adicionar um elemento a um conjunto, mas se o elemento já estiver presente no conjunto, a operação não terá efeito, pois os conjuntos não permitem elementos duplicados.