# Demonstração do método sort() em uma lista.

# Lista de linguagens.
linguagens = ["python", "js", "c", "java", "csharp"]

# Uso do método sort() para ordenar a lista em ordem alfabética crescente.
linguagens.sort()
print(linguagens)  # Resultado: ["c", "csharp", "java", "js", "python"]

# Uso do método sort() com o argumento reverse=True para ordenar a lista em ordem alfabética decrescente.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)  # Resultado: ["python", "js", "java", "csharp", "c"]

# Uso do método sort() com o argumento key para ordenar a lista com base no tamanho das strings.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # Resultado: ["c", "js", "java", "python", "csharp"]

# Uso do método sort() com os argumentos key e reverse=True para ordenar a lista em ordem decrescente de tamanho das strings.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # Resultado: ["python", "csharp", "java", "js", "c"]

#     A lista linguagens é criada com cinco elementos: "python", "js", "c", "java" e "csharp".

#     O método sort() é usado para ordenar a lista em ordem alfabética crescente (por padrão).

#     O método sort(reverse=True) é usado para ordenar a lista em ordem alfabética decrescente.

#     O método sort(key=lambda x: len(x)) é usado para ordenar a lista com base no tamanho das strings (número de caracteres).

#     O método sort(key=lambda x: len(x), reverse=True) é usado para ordenar a lista em ordem decrescente de tamanho das strings.

# Cada bloco demonstra diferentes formas de usar o método sort() para ordenar uma lista em Python.