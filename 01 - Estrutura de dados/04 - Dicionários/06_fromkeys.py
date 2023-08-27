# Criando um dicionário "resultado" usando o método "fromkeys()" com uma lista de chaves.
# Todas as chaves terão o valor padrão "None".
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# Criando um dicionário "resultado" usando o método "fromkeys()" com uma lista de chaves
# e um valor padrão fornecido ("vazio").
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# No primeiro exemplo, o método fromkeys() é usado para criar um dicionário com as chaves "nome" e "telefone", e o valor padrão associado a cada chave é None.

# No segundo exemplo, o método fromkeys() também é usado para criar um dicionário com as chaves "nome" e "telefone", mas dessa vez um valor padrão fornecido ("vazio") é associado a cada chave. Isso resulta em um dicionário em que ambas as chaves têm o valor "vazio".