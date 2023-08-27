contatos = {
    "wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verifica se a chave "wanderley@gmail.com" está presente no dicionário.
# Como está presente, o resultado será True.
resultado = "wanderley@gmail.com" in contatos
print(resultado)

# Verifica se a chave "megui@gmail.com" está presente no dicionário.
# Como não está presente, o resultado será False.
resultado = "megui@gmail.com" in contatos
print(resultado)

# Verifica se a chave "idade" está presente no dicionário associado à chave "wanderley@gmail.com".
# Como não está presente, o resultado será False.
resultado = "idade" in contatos["wanderley@gmail.com"]
print(resultado)

# Verifica se a chave "telefone" está presente no dicionário associado à chave "giovanna@gmail.com".
# Como está presente, o resultado será True.
resultado = "telefone" in contatos["giovanna@gmail.com"]
print(resultado)

# O código utiliza o operador in para verificar a presença de chaves no dicionário e para verificar a presença de uma chave específica nos dicionários aninhados. O resultado das verificações é um valor booleano (True ou False) que indica se a condição é verdadeira ou falsa.