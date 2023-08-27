contato = {"nome": "Wanderley", "telefone": "3333-2221"}

# O método "setdefault()" verifica se a chave "nome" já existe no dicionário.
# Como a chave "nome" já existe com o valor "Wanderley", o valor existente é retornado.
valor_retornado = contato.setdefault("nome", "Giovanna")  # "Wanderley"
print(valor_retornado)  # "Wanderley"
print(contato)  # {'nome': 'Wanderley', 'telefone': '3333-2221'}

# O método "setdefault()" verifica se a chave "idade" já existe no dicionário.
# Como a chave "idade" não existe, ela é adicionada com o valor 41.
valor_retornado = contato.setdefault("idade", 41)  # 41
print(valor_retornado)  # 41
print(contato)  # {'nome': 'Wanderley', 'telefone': '3333-2221', 'idade': 41}

# O método setdefault() é usado para obter o valor associado a uma chave no dicionário. Se a chave existir no dicionário, o método retornará o valor correspondente a essa chave. Caso contrário, ele adicionará a chave com um valor padrão (se fornecido) e retornará esse valor padrão. Se nenhum valor padrão for fornecido, ele adicionará a chave com o valor None. No exemplo acima, a chave "nome" já existia no dicionário, então o método não alterou o valor. No entanto, a chave "idade" não existia, então o método a adicionou com o valor 41.