# Demonstração do método extend() em uma lista.

# Lista de linguagens.
linguagens = ["python", "js", "c"]

# Impressão da lista original.
print(linguagens)  # Resultado: ["python", "js", "c"]

# Uso do método extend() para adicionar múltiplos elementos à lista.
linguagens.extend(["java", "csharp"])

# Impressão da lista após a extensão.
print(linguagens)  # Resultado: ["python", "js", "c", "java", "csharp"]

#     A lista linguagens é criada inicialmente com três elementos: "python", "js" e "c".

#     A linha print(linguagens) imprime a lista original, resultando em ["python", "js", "c"].

#     O método extend() é usado para adicionar múltiplos elementos à lista. Ele recebe uma lista (ou qualquer iterável) como argumento e adiciona cada elemento desse iterável à lista original.

#     A linha print(linguagens) após o uso do método extend() imprime a lista expandida, resultando em ["python", "js", "c", "java", "csharp"].

# O código demonstra como usar o método extend() para adicionar múltiplos elementos a uma lista em Python.