# Criando um dicionário chamado "contatos" que armazena informações sobre diferentes pessoas com seus e-mails como chaves.
contatos = {
    "wanderleybazan@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Acessando o valor associado ao e-mail "giovanna@gmail.com" e, em seguida, acessando o valor associado à chave "telefone".
# O valor "3443-2121" será armazenado na variável "telefone".
telefone = contatos["giovanna@gmail.com"]["telefone"]

# Imprimindo o valor da variável "telefone". A saída será: "3443-2121".
print(telefone)

# Nesse código, o dicionário "contatos" armazena informações sobre várias pessoas, onde os e-mails são usados como chaves. O valor associado ao e-mail "giovanna@gmail.com" é um subdicionário contendo informações como nome e telefone. O código acessa o telefone da pessoa associada ao e-mail "giovanna@gmail.com" e imprime esse número de telefone.