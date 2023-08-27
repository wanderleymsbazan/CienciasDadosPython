contatos = {"Wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Usando o método "popitem()" para remover e retornar um par chave-valor arbitrário do dicionário.
# O par chave-valor é retornado como uma tupla e a entrada é removida.
resultado = contatos.popitem()  # ("Wanderley@gmail.com', {'nome': 'Wanderley', 'telefone': '3333-2221'})
print(resultado)

# Tentando usar "popitem()" em um dicionário vazio resultará em um erro "KeyError".
# contatos.popitem()  # KeyError

# O método popitem() é usado para remover e retornar um par chave-valor arbitrário de um dicionário. Como os dicionários em Python 3.7+ são mantidos em uma ordem de inserção, essa operação retornará o último par chave-valor inserido no dicionário. A operação também remove esse par do dicionário. No entanto, se o dicionário estiver vazio, chamar popitem() resultará em um erro "KeyError".