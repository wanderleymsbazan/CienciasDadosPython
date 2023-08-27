contatos = {
    "wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remove a chave "telefone" do dicionário associado à chave "wanderley@gmail.com".
del contatos["wanderley@gmail.com"]["telefone"]

# Remove completamente a entrada com a chave "chappie@gmail.com" do dicionário.
del contatos["chappie@gmail.com"]

# O dicionário resultante após as remoções.
# Note que a entrada associada à chave "wanderley@gmail.com" teve a chave "telefone" removida.
# A entrada associada à chave "chappie@gmail.com" foi completamente removida.
print(contatos)

# A operação del é usada para excluir elementos específicos de um dicionário, e quando aplicada a uma chave de dicionário, remove a entrada correspondente. Se aplicada a uma chave aninhada em um dicionário, a operação del remove a chave e seu valor associado dentro do dicionário aninhado.