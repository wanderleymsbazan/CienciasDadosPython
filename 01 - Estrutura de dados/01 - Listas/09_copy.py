# Demonstração do método copy() em uma lista.

# Criação da lista com elementos diversos.
lista = [1, "Python", [40, 30, 20]]

# Uso do método copy() para criar uma cópia da lista.
lista.copy()

# Impressão da lista original (não modificada).
print(lista)  # Resultado: [1, "Python", [40, 30, 20]]

#     A lista lista é criada inicialmente com três elementos: o número 1, a string "Python" e uma lista [40, 30, 20].

#     A linha lista.copy() chama o método copy() na lista, que cria uma cópia da lista, mas essa cópia não está sendo atribuída a nenhuma variável. Portanto, essa cópia é descartada e não é utilizada.

#     A linha print(lista) imprime a lista original, que permanece inalterada, resultando em [1, "Python", [40, 30, 20]].

# O código não demonstra o uso efetivo da cópia criada pelo método copy(), uma vez que a cópia não é armazenada ou usada posteriormente no código.