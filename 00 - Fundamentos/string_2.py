# Formatação de strings em Python.

nome = "Wanderley"
idade = 41
profissao = "Progamador"
linguagem = "Python"
saldo = 263.000

dados = {"nome": "Wanderley", "idade": 41}

# Utilização do operador '%' para formatação de string (versão antiga).
print("Nome: %s Idade: %d" % (nome, idade))

# Utilização do método 'format()' para formatação de string (Python 2 e 3).
print("Nome: {} Idade: {}".format(nome, idade))

# Utilização do método 'format()' com índices para reordenar os argumentos.
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# Utilização do método 'format()' com nomes de campos especificados.
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

# Utilização do método 'format()' com unpacking de dicionário.
print("Nome: {nome} Idade: {idade}".format(**dados))

# Utilização de f-strings (format strings) - Python 3.6 e superior.
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

#     Variáveis como nome, idade, profissao, linguagem e saldo contêm informações diversas.

#     O operador % é utilizado para formatação de string, mas é considerado uma abordagem mais antiga. É possível formatar usando %s para strings e %d para inteiros.

#     A função format() é usada para formatar strings. As chaves {} são usadas como marcadores de substituição.

#     É possível reordenar os argumentos usando índices dentro das chaves {}.

#     A formatação pode ser realizada usando nomes de campos especificados.

#     Com um dicionário dados, é possível usar o método format() com unpacking de dicionário.

#     F-strings (format strings) são uma maneira mais recente e conveniente de formatar strings, introduzida no Python 3.6. Você pode incluir expressões dentro das chaves {} e usar formatação avançada, como limitar casas decimais em números.

# O código demonstra diferentes maneiras de formatar strings em Python, incluindo o uso de % (mais antigo), o método format() (usado em Python 2 e 3) e f-strings (introduzidas no Python 3.6).