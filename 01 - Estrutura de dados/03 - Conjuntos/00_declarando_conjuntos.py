# Demonstração da criação de conjuntos em Python.

# Criando um conjunto de números.
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # Resultado: {1, 2, 3, 4}

# Criando um conjunto de letras.
letras = set("abacaxi")
print(letras)  # Resultado: {"b", "a", "c", "x", "i"}

# Criando um conjunto de carros.
carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # Resultado: {"gol", "celta", "palio"}

#     No primeiro exemplo, um conjunto numeros é criado a partir de uma lista que contém elementos repetidos (1, 2, 3, 1, 3, 4). Quando o conjunto é criado, automaticamente os elementos duplicados são removidos, resultando no conjunto {1, 2, 3, 4}.

#     No segundo exemplo, um conjunto letras é criado a partir da string "abacaxi". Da mesma forma, os elementos duplicados ("a") são removidos, resultando no conjunto {"b", "a", "c", "x", "i"}.

#     No terceiro exemplo, um conjunto carros é criado a partir de uma tupla que contém elementos repetidos ("palio"). Os elementos duplicados são removidos, resultando no conjunto {"gol", "celta", "palio"}.

# Os conjuntos em Python são uma estrutura de dados que armazena elementos únicos, não mantendo repetições de elementos.