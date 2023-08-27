texto = input("Informe um texto: ")  # Solicita ao usuário que insira um texto.
VOGAIS = "AEIOU"  # Definição das vogais maiúsculas.

# Itera sobre cada letra no texto inserido.
for letra in texto:
    # Verifica se a letra (convertida para maiúscula) está entre as vogais definidas.
    if letra.upper() in VOGAIS:
        print(letra, end="")  # Se for uma vogal, imprime a letra, sem quebra de linha.
else:
    print()  # Adiciona uma quebra de linha após o loop.

#Nesse trecho, o código solicita ao usuário que insira um texto. Em seguida, ele percorre cada letra do texto inserido. Se a letra (convertida para maiúscula) estiver entre as vogais definidas na constante VOGAIS, ela é impressa sem quebra de linha. O else após o loop adiciona uma quebra de linha.

# Itera sobre uma sequência de números de 0 a 50, com incremento de 5.
for numero in range(0, 51, 5):
    print(numero, end=" ")  # Imprime os números separados por espaço.

#Nesse segundo trecho, o código utiliza um loop for para iterar sobre uma sequência de números de 0 a 50, com incremento de 5 a cada iteração. Ele imprime cada número na mesma linha, separados por espaço.
#Ambos os exemplos ilustram a utilização de loops for e demonstram diferentes formas de iteração em Python: percorrendo um iterável (como uma string) e utilizando a função range para gerar uma sequência numérica.