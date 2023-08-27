# Definição do saldo atual e valor de saque.
saldo = 2000
saque = 2500

# Uso da expressão condicional (ternário) para determinar o status da operação de saque.
status = "Sucesso" if saldo >= saque else "Falha"

# Impressão do resultado utilizando f-string.
print(f"{status} ao realizar o saque!")

#Neste código, a expressão condicional (ternário) é usada para verificar se o saldo é suficiente para realizar o saque. Se a condição saldo >= saque for verdadeira, o valor da variável status será "Sucesso", caso contrário, será "Falha". Em seguida, a f-string é usada para imprimir o resultado da operação de saque, que será "Sucesso ao realizar o saque!" se o saldo for suficiente ou "Falha ao realizar o saque!" se o saldo for insuficiente.