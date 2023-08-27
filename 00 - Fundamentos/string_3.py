# Acesso e manipulação de strings usando índices e slicing.

nome = "Wanderley Marangoni Sanches Bazan"

# Acessa o primeiro caractere da string.
print(nome[0])  # Resultado: 'W'

# Acessa o penúltimo caractere da string.
print(nome[-2])  # Resultado: 'z'

# Faz slicing da string até o índice 9 (exclusivo).
print(nome[:9])  # Resultado: 'Wanderley'

# Faz slicing da string a partir do índice 10.
print(nome[10:])  # Resultado: 'Marangoni Sanches Bazan'

# Faz slicing da string do índice 10 até o 16 (exclusivo).
print(nome[10:16])  # Resultado: 'Marang'

# Faz slicing da string do índice 10 até o 16 (exclusivo), pulando de 2 em 2.
print(nome[10:16:2])  # Resultado: 'Mrg'

# Faz slicing da string completa (cópia da string original).
print(nome[:])  # Resultado: 'Wanderley Marangoni Sanches Bazan'

# Faz slicing da string completa em ordem reversa.
print(nome[::-1])  # Resultado: 'nazaB sehcnaS inognaM yeldreW'

#     A string nome contém o valor "Wanderley Marangoni Sanches Bazan".

#     O acesso a caracteres individuais em uma string é feito usando índices. nome[0] acessa o primeiro caractere ('W') e nome[-2] acessa o penúltimo caractere ('z').

#     O slicing nome[:9] pega os caracteres da posição 0 até a posição 9 (exclusivo), resultando em "Wanderley".

#     O slicing nome[10:] pega os caracteres a partir da posição 10 até o final da string, resultando em "Marangoni Sanches Bazan".

#     O slicing nome[10:16] pega os caracteres da posição 10 até a posição 16 (exclusivo), resultando em "Marang".

#     O slicing nome[10:16:2] faz o mesmo slicing anterior, mas pula de 2 em 2 caracteres, resultando em "Mrg".

#     O slicing nome[:] cria uma cópia da string completa.

#     O slicing nome[::-1] faz o slicing da string completa em ordem reversa, resultando em "nazaB sehcnaS inognaM yeldreW".

# O código demonstra novamente operações de acesso e manipulação de strings usando índices e slicing em Python. Note que os resultados diferem um pouco das explicações anteriores devido às diferenças na string de exemplo.
