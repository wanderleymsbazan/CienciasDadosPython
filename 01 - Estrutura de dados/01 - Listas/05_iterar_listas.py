# Demonstração de loops for com listas e uso de enumerate.

# Lista de carros.
carros = ["gol", "celta", "palio"]

# Loop for para percorrer e imprimir cada carro da lista.
for carro in carros:
    print(carro)
# Resultado:
# gol
# celta
# palio

# Loop for com uso da função enumerate para obter índice e valor.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
# Resultado:
# 0: gol
# 1: celta
# 2: palio

#     A lista carros contém três elementos: "gol", "celta" e "palio".

#     O primeiro loop for itera através da lista carros e imprime cada carro da lista, um por linha.

#     O segundo loop for utiliza a função enumerate() para percorrer a lista carros e obter tanto o índice quanto o valor em cada iteração. Isso permite imprimir o índice e o valor de cada carro no formato "índice: valor".

# O código demonstra como usar loops for para iterar através de listas e como utilizar a função enumerate() para obter índices e valores durante a iteração.