# Criando um dicionário chamado "contatos" que armazena informações sobre diferentes pessoas com seus e-mails como chaves.
contatos = {
    "wanderleybazan@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Utilizando o método "clear()" para remover todos os itens do dicionário "contatos".
contatos.clear()

# Imprimindo o dicionário após a remoção dos itens, que resultará em um dicionário vazio.
print(contatos)  # {}

# Nesse código, o método clear() é usado para remover todos os itens do dicionário "contatos", deixando-o vazio. Quando o dicionário é impresso após a aplicação do método clear(), você verá que ele não contém mais nenhum item.