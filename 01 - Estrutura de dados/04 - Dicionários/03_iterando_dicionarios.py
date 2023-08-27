# Criando um dicionário chamado "contatos" que armazena informações sobre diferentes pessoas com seus e-mails como chaves.
contatos = {
    "wanderleybazan@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iterando sobre as chaves do dicionário "contatos" e imprimindo a chave e o valor associado a ela.
for chave in contatos:
    print(chave, contatos[chave])

# Imprimindo uma linha de separação para melhor visualização.
print("=" * 100)

# Iterando sobre os itens (chave-valor) do dicionário "contatos" e imprimindo a chave e o valor associado a ela.
for chave, valor in contatos.items():
    print(chave, valor)

# Nesse código, o primeiro loop for itera sobre as chaves do dicionário "contatos" e imprime a chave e o valor associado a essa chave. O segundo loop for utiliza o método items() para iterar sobre os itens (chave-valor) do dicionário e imprime a chave e o valor associado a ela. Ambos os loops produzirão a mesma saída, exibindo as informações de contato para cada pessoa no dicionário "contatos".