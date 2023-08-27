# Define a função que aceita argumentos posicionais até a barra e depois argumentos nomeados marcados por '*'.
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    # Imprime os valores recebidos como argumentos.
    print(modelo, ano, placa, marca, motor, combustivel)

# Chama a função 'criar_carro' passando argumentos nomeados após a barra e marcados por '*'.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Inválido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# A primeira chamada de função está comentada porque ela tenta passar argumentos posicionais após a barra /, o que não é permitido de acordo com a definição da função. A segunda chamada de função é válida, pois passa os argumentos nomeados após a barra e marcados por *, conforme o esperado pela função.
