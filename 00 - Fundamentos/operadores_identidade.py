saldo = 1000  # Atribuição do valor 1000 à variável saldo.
limite = 1000  # Atribuição do valor 1000 à variável limite.

# Verifica se a variável saldo é a mesma referência de memória que a variável limite.
print(saldo is limite)

# Verifica se a variável saldo não é a mesma referência de memória que a variável limite.
print(saldo is not limite)

#     A variável saldo é atribuída com o valor 1000, e a variável limite também é atribuída com o valor 1000.

#     A expressão saldo is limite verifica se as variáveis saldo e limite referem-se à mesma referência de memória. Nesse caso, como os valores são iguais e são objetos imutáveis, ambos podem apontar para o mesmo local de memória. Portanto, a expressão resulta em True.

#     A expressão saldo is not limite verifica se as variáveis saldo e limite não referem-se à mesma referência de memória. Como no caso anterior, eles podem apontar para o mesmo local de memória. No entanto, nesse caso, a expressão resulta em False.

# A utilização de is e is not para comparação de variáveis verifica se elas referem-se ao mesmo objeto em memória, não apenas se possuem valores iguais. Em geral, isso é mais relevante para objetos mutáveis, enquanto para valores inteiros (como nesse caso), a igualdade de valores é mais importante.