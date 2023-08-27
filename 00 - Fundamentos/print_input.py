# Solicita ao usuário que informe seu nome e idade.
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

# Imprime o nome e a idade separados por espaço.
print(nome, idade)

# Imprime o nome e a idade separados por espaço, e adiciona "..." no final.
print(nome, idade, end="...\n")

# Imprime o nome e a idade separados pelo caractere "#" e adiciona "..." no final.
print(nome, idade, sep="#", end="...\n")

# Imprime o nome e a idade separados pelo caractere "#".
print(nome, idade, sep="#")

#     A função input() é usada para receber entrada do usuário e armazenar o valor na variável nome e idade.

#     A primeira linha print(nome, idade) imprime o valor de nome e idade, separados por um espaço.

#     A segunda linha print(nome, idade, end="...\n") faz a mesma impressão anterior, mas adiciona "..." no final usando o argumento end.

#     A terceira linha print(nome, idade, sep="#", end="...\n") usa o argumento sep para separar o valor de nome e idade com o caractere "#", e também adiciona "..." no final.

#     A quarta linha print(nome, idade, sep="#") imprime o valor de nome e idade separados pelo caractere "#".

# O código demonstra o uso da função input() para receber entrada do usuário e a função print() para exibir as informações com diferentes formatações e configurações de separadores e caracteres de fim de linha.