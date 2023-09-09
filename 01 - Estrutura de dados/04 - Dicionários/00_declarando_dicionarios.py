# Criando um dicionário chamado "pessoa" com as informações iniciais de nome e idade.
pessoa = {"nome": "Wanderley", "idade": 41}

# Imprimindo o dicionário "pessoa" na saída.
print(pessoa) 

# Criando um novo dicionário "pessoa" usando a função dict e passando os valores como argumentos nomeados.
pessoa = dict(nome="Wanderley", idade=41)

# Imprimindo o novo dicionário "pessoa" na saída.
print(pessoa)

# Adicionando uma nova chave-valor ao dicionário "pessoa".
# Agora o dicionário inclui também o campo "telefone" com o valor "3333-1234".
pessoa["telefone"] = "3333-1234"

# Imprimindo o dicionário "pessoa" atualizado na saída.
print(pessoa)

#     pessoa = {"nome": "Wanderley", "idade": 41}:
#         Neste passo, estamos criando um dicionário chamado "pessoa" com duas chaves-valor: "nome" com o valor "Wanderley" e "idade" com o valor 41.

#     print(pessoa):
#         Aqui, estamos imprimindo o dicionário "pessoa" na saída. O resultado será {"nome": "Wanderley", "idade": 41}.

#     pessoa = dict(nome="Wanderley", idade=41):
#         Neste ponto, estamos criando um novo dicionário "pessoa" usando a função dict(). Em vez de usar chaves, estamos passando os valores diretamente como argumentos nomeados, ou seja, nome="Wanderley" e idade=41.

#     print(pessoa):
#         Estamos imprimindo o novo dicionário "pessoa" na saída. O resultado será novamente {"nome": "Wanderley", "idade": 41}. Isso acontece porque recriamos o dicionário com as mesmas informações.

#     pessoa["telefone"] = "3333-1234":
#         Neste trecho, estamos adicionando uma nova chave-valor ao dicionário "pessoa". A chave é "telefone" e o valor é "3333-1234".

#     print(pessoa):
#         Finalmente, estamos imprimindo o dicionário "pessoa" atualizado na saída. Agora ele possui três pares chave-valor: {"nome": "Wanderley", "idade": 41, "telefone": "3333-1234"}.

# Em resumo, o código cria e manipula um dicionário chamado "pessoa" que armazena informações como nome, idade e telefone. Ele demonstra como criar dicionários usando diferentes abordagens e como adicionar novos elementos a eles.