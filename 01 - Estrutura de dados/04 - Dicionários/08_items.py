contatos = {"wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Usando o método "items()" para obter uma vista dos itens (chave-valor) do dicionário.
# O resultado é um objeto do tipo "dict_items" contendo as entradas do dicionário.
resultado = contatos.items()  # dict_items([('wanderley@gmail.com', {'nome': 'Wanderley', 'telefone': '3333-2221'})])
print(resultado)

# O método items() retorna uma vista iterável dos itens do dicionário, onde cada item é uma tupla contendo a chave e o valor correspondente. Nesse caso, o resultado é uma vista contendo a única entrada do dicionário contatos, que é uma chave "wanderley@gmail.com" associada a um dicionário contendo informações sobre "Wanderley".