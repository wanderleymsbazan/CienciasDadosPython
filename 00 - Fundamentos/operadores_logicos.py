# Demonstração do uso dos operadores lógicos AND e OR.

# Uso do operador AND: Todos os valores devem ser True para a expressão ser True.
print(True and True and True)  # Resultado: True
print(True and False and True)  # Resultado: False
print(False and False and False)  # Resultado: False

# Uso do operador OR: Pelo menos um valor deve ser True para a expressão ser True.
print(True or True or True)  # Resultado: True
print(True or False or False)  # Resultado: True
print(False or False or False)  # Resultado: False

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Criação de uma expressão complexa usando os operadores lógicos.
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # Resultado: True, pois a expressão é verdadeira.

# A mesma expressão, mas com parênteses para definir a ordem de avaliação.
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  # Resultado: True, novamente a expressão é verdadeira.

# Divisão da expressão complexa em partes separadas.
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

# Combinação das partes separadas usando o operador OR.
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)  # Resultado: True, a expressão ainda é verdadeira.

#     As primeiras linhas demonstram o uso dos operadores lógicos AND e OR com valores booleanos. AND retorna True apenas quando todos os operandos são True, enquanto OR retorna True se pelo menos um operando for True.

#     As variáveis saldo, saque, limite e conta_especial são definidas com valores. Essas variáveis são usadas para demonstrar a construção de expressões complexas.

#     A variável exp contém uma expressão complexa que combina várias condições usando os operadores AND e OR. O resultado é impresso e é True porque a expressão é verdadeira.

#     A variável exp_2 contém a mesma expressão complexa, mas usando parênteses para garantir a ordem de avaliação correta. O resultado também é True.

#     As variáveis conta_normal_com_saldo_suficiente e conta_especial_com_saldo_suficiente dividem a expressão complexa original em partes mais legíveis.

#     A variável exp_3 combina as partes usando o operador OR, e o resultado é novamente True.

# O código demonstra o uso dos operadores lógicos AND e OR para construir expressões complexas que envolvem condições booleanas.