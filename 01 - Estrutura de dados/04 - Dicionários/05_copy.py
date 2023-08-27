# Criando um dicionário chamado "contatos" que armazena informações sobre uma pessoa com seu e-mail como chave.
contatos = {"Wanderley@gmail.com": {"nome": "Wanderley", "telefone": "3333-2221"}}

# Criando uma cópia do dicionário "contatos" usando o método "copy()".
copia = contatos.copy()

# Modificando o valor associado à chave "Wanderley@gmail.com" na cópia.
copia["Wanderley@gmail.com"] = {"nome": "Wander"}

# Imprimindo o valor associado à chave "Wanderley@gmail.com" no dicionário original.
print(contatos["Wanderley@gmail.com"])  # {"nome": "Wanderley", "telefone": "3333-2221"}

# Imprimindo o valor associado à chave "Wanderley@gmail.com" na cópia modificada.
print(copia["Wanderley@gmail.com"])  # {"nome": "Wander"}

# Nesse código, é feita uma cópia do dicionário "contatos" utilizando o método copy(). Após criar a cópia, é modificado o valor associado à chave "Wanderley@gmail.com" na cópia. Isso não afeta o valor no dicionário original. No final, ao imprimir os valores associados à mesma chave em ambos os dicionários, você verá que eles são diferentes devido à modificação na cópia.