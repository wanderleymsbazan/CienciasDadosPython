contatos = {"wanderley@gmail.com": {"nome": "wanderley", "telefone": "3333-2221"}}

# Atualiza o valor associado à chave "wanderley@gmail.com" no dicionário.
# Nesse caso, a chave já existe, então o valor é atualizado para {"nome": "Wander"}.
contatos.update({"wanderley@gmail.com": {"nome": "Wander"}})
print(contatos)  # {'wanderley@gmail.com': {'nome': 'Wander'}}

# Adiciona uma nova entrada no dicionário com a chave "giovanna@gmail.com"
# e o valor {"nome": "Giovanna", "telefone": "3322-8181"}.
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)
# {'wanderley@gmail.com': {'nome': 'Wander'},
#  'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

# O método update() é usado para adicionar ou atualizar entradas em um dicionário com base em outro dicionário (ou em pares chave-valor). Se a chave já existir no dicionário, o valor correspondente será atualizado. Se a chave não existir, uma nova entrada será adicionada com a chave e valor fornecidos. No exemplo acima, a chave "wanderley@gmail.com" já existia no dicionário, então o valor foi atualizado para {"nome": "Wander"}. Além disso, uma nova entrada foi adicionada com a chave "giovanna@gmail.com" e o valor correspondente.