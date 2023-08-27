contatos = {"wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Usando o método "keys()" para obter uma vista das chaves do dicionário.
# O resultado é um objeto do tipo "dict_keys" contendo as chaves do dicionário.
resultado = contatos.keys()  # dict_keys(['wanderley@gmail.com'])
print(resultado)

# O método keys() retorna uma vista iterável das chaves presentes no dicionário. Nesse caso, o resultado é uma vista contendo a única chave "wanderley@gmail.com" presente no dicionário contatos.