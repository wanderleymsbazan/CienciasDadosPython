contatos = {"Wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Tentando acessar uma chave ("chave") que não existe no dicionário.
# Isso resultaria em um erro KeyError.
# contatos["chave"]  # KeyError

# Usando o método "get()" para obter o valor associado a uma chave que não existe no dicionário.
# Nesse caso, como a chave "chave" não existe, o método retorna o valor padrão "None".
resultado = contatos.get("chave")  # None
print(resultado)

# Usando o método "get()" com um valor padrão vazio (dicionário vazio) caso a chave não exista.
# Isso resulta em um dicionário vazio sendo retornado.
resultado = contatos.get("chave", {})  # {}
print(resultado)

# Usando o método "get()" para obter o valor associado à chave "Wanderley@gmail.com".
# Como essa chave existe no dicionário, o método retorna o valor correspondente.
resultado = contatos.get(
    "Wanderley@gmail.com", {}
)  # {"Wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}
print(resultado)

# O método get() é usado para acessar o valor associado a uma chave em um dicionário. Ele recebe dois argumentos: a chave que você deseja acessar e um valor padrão opcional que é retornado se a chave não existir no dicionário. Se a chave existir, o método retorna o valor correspondente a essa chave; caso contrário, retorna o valor padrão (ou None se nenhum valor padrão for fornecido).
