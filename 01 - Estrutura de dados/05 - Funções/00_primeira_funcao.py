# Define uma função sem parâmetros que imprime uma mensagem fixa.
def exibir_mensagem():
    print("Olá mundo!")

# Define uma função com um parâmetro 'nome' que imprime uma mensagem personalizada.
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Define uma função com um parâmetro opcional 'nome' que imprime uma mensagem personalizada.
# Se o nome não for fornecido, assume o valor padrão "Anônimo".
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Chama a primeira função sem argumentos.
exibir_mensagem()

# Chama a segunda função, passando o argumento 'nome' como "Wanderley".
exibir_mensagem_2(nome="Wanderley")

# Chama a terceira função sem fornecer argumentos, usando o valor padrão "Anônimo".
exibir_mensagem_3()

# Chama a terceira função, passando o argumento 'nome' como "Chappie".
exibir_mensagem_3(nome="Chappie")

nome = input("Digite o seu nome: ")
exibir_mensagem_3(nome=nome)

