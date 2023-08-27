# Criação de uma cópia de um conjunto usando o método copy().

# Inicializando um conjunto chamado "sorteio".
sorteio = {1, 23}

# Exibindo o conjunto antes da cópia.
print(sorteio)  # Resultado: {1, 23}

# Usando o método copy() para criar uma cópia do conjunto "sorteio".
sorteio.copy()

# Exibindo o conjunto após a cópia (o conjunto original não é modificado).
print(sorteio)  # Resultado: {1, 23}

#     Você começa inicializando um conjunto chamado "sorteio" com os elementos 1 e 23.

#     O método copy() é usado para criar uma cópia de um conjunto. No entanto, na sua implementação atual, você está chamando o método copy(), mas não está armazenando a cópia em uma variável ou utilizando-a de alguma forma. Como resultado, o conjunto "sorteio" permanece inalterado após a chamada do método copy().

# Se você deseja criar uma cópia do conjunto e armazená-la em uma nova variável, você pode fazer o seguinte:
sorteio = {1, 23}

copia_sorteio = sorteio.copy()

print(sorteio)  # Resultado: {1, 23}
print(copia_sorteio)  # Resultado: {1, 23}

# Dessa forma, o conjunto "copia_sorteio" conterá uma cópia idêntica dos elementos presentes no conjunto "sorteio".