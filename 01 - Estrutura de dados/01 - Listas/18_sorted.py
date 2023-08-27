# Demonstração da função sorted() com argumento key em uma lista.

# Lista de linguagens.
linguagens = ["python", "js", "c", "java", "csharp"]

# Uso da função sorted() com argumento key para ordenar a lista com base no tamanho das strings.
print(sorted(linguagens, key=lambda x: len(x)))  # Resultado: ["c", "js", "java", "python", "csharp"]

# Uso da função sorted() com argumentos key e reverse para ordenar a lista em ordem decrescente de tamanho das strings.
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # Resultado: ["python", "csharp", "java", "js", "c"]

#     A lista linguagens é criada com cinco elementos: "python", "js", "c", "java" e "csharp".

#     A função sorted() é usada para ordenar a lista com base no tamanho das strings, usando o argumento key e uma função lambda lambda x: len(x).

#     A função sorted(linguagens, key=lambda x: len(x)) resulta em ["c", "js", "java", "python", "csharp"], que é a lista ordenada pelo tamanho das strings de forma crescente.

#     A função sorted(linguagens, key=lambda x: len(x), reverse=True) resulta em ["python", "csharp", "java", "js", "c"], que é a lista ordenada pelo tamanho das strings de forma decrescente.

# O código demonstra como usar a função sorted() com argumentos key e reverse para ordenar uma lista com base em uma chave específica e em ordem crescente ou decrescente.