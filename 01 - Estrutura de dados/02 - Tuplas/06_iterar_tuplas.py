# Iterando sobre uma tupla usando um loop for.

# Tupla de carros.
carros = (
    "gol",
    "celta",
    "palio",
)

# Iteração simples sobre a tupla usando um loop for.
for carro in carros:
    print(carro)

# Iteração com obtenção dos índices usando a função enumerate().
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#     A tupla carros é criada com três elementos: "gol", "celta" e "palio".

#     No primeiro loop for, cada elemento da tupla é iterado sequencialmente e impresso.

#     No segundo loop for, a função enumerate() é usada para obter tanto o índice quanto o valor do elemento durante a iteração. Isso permite imprimir o índice juntamente com o valor do carro.

# O código demonstra como percorrer uma tupla usando um loop for e como usar a função enumerate() para obter índices durante a iteração.