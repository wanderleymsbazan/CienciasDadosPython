# Define a função 'somar' que recebe dois argumentos e retorna sua soma.
def somar(a, b):
    return a + b

# Define a função 'exibir_resultado' que recebe dois números e uma função como argumentos.
# Ela chama a função passada como argumento e exibe o resultado da operação.
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)  # Chama a função passada como argumento.
    print(f"O resultado da operação {a} + {b} = {resultado}")

# Chama a função 'exibir_resultado' passando os números 10 e 10, e a função 'somar'.
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

# Na chamada exibir_resultado(10, 10, somar), a função somar é passada como argumento para a função exibir_resultado, que a chama internamente para calcular o resultado e exibir a mensagem com o valor da soma.