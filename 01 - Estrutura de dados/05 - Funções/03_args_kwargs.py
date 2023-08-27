# Define a função que aceita uma data por extenso, uma série de versos e metadados opcionais.
def exibir_poema(data_extenso, *args, **kwargs):
    # Junta os versos em um único bloco de texto separado por quebras de linha.
    texto = "\n".join(args)
    
    # Cria uma string formatada com os metadados fornecidos.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    
    # Combina a data, os versos e os metadados em uma única mensagem formatada.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
    # Imprime a mensagem.
    print(mensagem)

# Chama a função 'exibir_poema' passando argumentos posicionais e nomeados.
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    # ...
    autor="Tim Peters",
    ano=1999,
)
