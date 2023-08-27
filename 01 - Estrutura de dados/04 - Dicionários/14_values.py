contatos = {
    "wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# O método values() é usado para obter uma visão dos valores no dicionário.
# No caso, a saída será um objeto dict_values contendo os valores associados a cada chave.
resultado = contatos.values()

# Imprime o resultado, que será uma visão dos valores no dicionário.
# Cada valor é um dicionário que contém informações sobre a pessoa.
print(resultado)

# O método values() retorna uma visão dos valores contidos no dicionário. Nesse caso, os valores são dicionários que contêm informações sobre cada pessoa nos contatos. A saída será um objeto dict_values que fornece uma visão dos valores. Cada valor é um dicionário que contém os detalhes da pessoa, como nome e telefone. Note que a ordem dos valores na saída pode não ser a mesma ordem em que foram inseridos no dicionário, pois os dicionários em Python não garantem uma ordem específica para seus elementos.