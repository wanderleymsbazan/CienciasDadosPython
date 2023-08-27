contatos = {"wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Usando o método "pop()" para remover uma entrada do dicionário.
# O valor associado à chave "wanderley@gmail.com" é retornado e a entrada é removida.
resultado = contatos.pop("wanderley@gmail.com")  # {'nome': 'Wanderley', 'telefone': '3333-2221'}
print(resultado)

# Usando o método "pop()" com um valor padrão.
# Se a chave "wanderley@gmail.com" não existir, o valor padrão {} é retornado.
resultado = contatos.pop("wanderley@gmail.com", {})  # {}
print(resultado)

# O método pop() é usado para remover uma entrada de um dicionário com base em sua chave. Se a chave existir no dicionário, o valor associado a ela é retornado e a entrada é removida. Se a chave não existir, o valor padrão fornecido (no segundo argumento) é retornado. No primeiro caso, a chave "wanderley@gmail.com" existe no dicionário, portanto, o valor associado é retornado e a entrada é removida. No segundo caso, como a chave não existe, o valor padrão {} é retornado.