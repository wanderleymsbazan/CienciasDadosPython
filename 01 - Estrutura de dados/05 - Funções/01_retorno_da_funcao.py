# Define uma função que recebe uma lista de números e retorna a soma deles.
def calcular_total(numeros):
    return sum(numeros)

# Define uma função que recebe um número e retorna seu antecessor e sucessor.
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    # Retorna uma tupla com o antecessor e o sucessor.
    return antecessor, sucessor

# Chama a função 'calcular_total' passando uma lista de números.
print(calcular_total([10, 20, 34]))  # 64

# Chama a função 'retorna_antecessor_e_sucessor' passando o número 10.
# A função retorna uma tupla com o antecessor (9) e o sucessor (11).
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
