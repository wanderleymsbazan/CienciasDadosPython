# Manipulação de strings e formatação.

nome = "WaNdeRleY"

# Converte todos os caracteres da string para maiúsculas.
print(nome.upper())

# Converte todos os caracteres da string para minúsculas.
print(nome.lower())

# Converte a primeira letra de cada palavra para maiúscula.
print(nome.title())

texto = "  Olá mundo!    "

# Concatena um ponto no final da string texto.
print(texto + ".")

# Remove espaços em branco do início e fim da string texto, e depois concatena um ponto.
print(texto.strip() + ".")

# Remove espaços em branco do final da string texto, e depois concatena um ponto.
print(texto.rstrip() + ".")

# Remove espaços em branco do início da string texto, e depois concatena um ponto.
print(texto.lstrip() + ".")

menu = "Python"

# Adiciona caracteres "#" antes e depois da string menu.
print("####" + menu + "####")

# Centraliza a string menu dentro de um espaço de 14 caracteres.
print(menu.center(14))

# Centraliza a string menu dentro de um espaço de 14 caracteres, preenchendo com "#".
print(menu.center(14, "#"))

# Junta os caracteres da string menu com o caractere "-" entre eles.
print("-".join(menu))

#     A variável nome contém o valor "WaNdeRleY". As funções upper(), lower() e title() são usadas para manipular o formato da string e imprimir o nome em letras maiúsculas, minúsculas e com cada palavra iniciando em maiúscula.

#     A variável texto contém a string " Olá mundo! ". A função strip() remove espaços em branco do início e do fim da string.

#     A função rstrip() remove espaços em branco apenas do final da string, e a função lstrip() remove espaços em branco apenas do início da string.

#     A variável menu contém a string "Python". As operações de concatenação e formatação são usadas para criar uma barra lateral decorativa ao redor do texto.

#     A função center() centraliza a string menu dentro de um espaço definido, e a função join() insere o caractere "-" entre cada caractere da string menu.

# O código demonstra várias operações de manipulação de strings em Python, incluindo transformação de maiúsculas/minúsculas, remoção de espaços em branco, centralização e formatação.