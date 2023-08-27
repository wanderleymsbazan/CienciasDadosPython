# Define a variável global 'salario' com o valor inicial de 2000.
salario = 2000

# Define a função 'salario_bonus' que recebe um bônus como argumento.
# Ela incrementa o bônus ao valor global do 'salario' e retorna o novo valor.
def salario_bonus(bonus):
    global salario  # Indica que a variável 'salario' a ser usada é a global.
    salario += bonus  # Incrementa o bônus ao 'salario'.
    return salario  # Retorna o novo valor do 'salario'.

# Chama a função 'salario_bonus' passando um bônus de 500.
# O valor global do 'salario' é incrementado em 500, resultando em 2500.
salario_bonus(500)  # 2500

# É importante notar o uso da declaração global dentro da função salario_bonus, que indica que a variável salario a ser modificada é a variável global, não uma variável local. Isso permite que a função altere o valor da variável global salario.