# Define uma função que recebe informações sobre um carro e as imprime.
def salvar_carro(marca, modelo, ano, placa):
    # Simula a ação de salvar o carro no banco de dados e imprime uma mensagem.
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chama a função 'salvar_carro' passando os argumentos diretamente na ordem correta.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chama a função 'salvar_carro' usando argumentos nomeados para melhor clareza.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Chama a função 'salvar_carro' usando a sintaxe de unpacking de dicionário (double asterisk **).
# O dicionário contém os argumentos nomeados que serão desempacotados e passados para a função.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
