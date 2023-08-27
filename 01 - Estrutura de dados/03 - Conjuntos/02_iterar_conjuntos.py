# Iterando sobre um conjunto usando um loop for.

# Conjunto de carros.
carros = {"gol", "celta", "palio"}

# Iterando sobre o conjunto e exibindo os carros.
for carro in carros:
    print(carro)

# Iterando sobre o conjunto usando enumerate() para obter índices e exibindo os carros.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#     No primeiro loop for, o conjunto carros é percorrido, e a variável carro recebe cada um dos elementos do conjunto. O código print(carro) exibe o nome de cada carro individualmente.

#     No segundo loop for, a função enumerate(carros) é usada para obter tanto o índice quanto o elemento de cada carro no conjunto. A variável indice recebe o índice do elemento, e a variável carro recebe o próprio elemento. O código print(f"{indice}: {carro}") exibe o índice seguido do nome do carro.

# Esses loops demonstram como iterar sobre conjuntos e como usar enumerate() para obter índices ao iterar sobre coleções.