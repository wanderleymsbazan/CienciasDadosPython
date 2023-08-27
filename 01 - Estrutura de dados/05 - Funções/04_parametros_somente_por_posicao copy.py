# Define a função que aceita argumentos posicionais e nomeados, com um sinal de barra para separá-los.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # Imprime os valores recebidos como argumentos.
    print(modelo, ano, placa, marca, motor, combustivel)

# Chama a função 'criar_carro' passando argumentos posicionais e nomeados.
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# cria_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Inválido

# A função criar_carro aceita primeiramente os argumentos posicionais (modelo, ano, placa) e depois os argumentos nomeados (marca, motor, combustivel). O uso do sinal de barra antes dos argumentos nomeados (/) indica que os argumentos antes da barra são obrigatoriamente posicionais, e os argumentos após a barra são nomeados.

# A segunda chamada de função, que está comentada, é inválida porque tenta passar os argumentos usando a forma nomeada antes do sinal de barra, o que não é permitido conforme a definição da função.
