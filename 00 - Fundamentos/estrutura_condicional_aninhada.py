# Definições dos tipos de conta e seus estados.
conta_normal = False
conta_universitaria = False
conta_especial = True

# Saldo atual, valor de saque e limite de cheque especial.
saldo = 2000
saque = 1500
cheque_especial = 450

# Verifica qual tipo de conta está selecionado e executa a lógica correspondente.
if conta_normal:
    # Se a conta for do tipo normal, verifica se há saldo suficiente ou se pode usar o cheque especial.
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    # Se a conta for do tipo universitária, verifica se há saldo suficiente.
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    # Se a conta for do tipo especial, imprime uma mensagem indicando a seleção.
    print("Conta especial selecionada!")

else:
    # Se nenhum dos tipos de conta for reconhecido, imprime uma mensagem de erro.
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")

#Esse código simula diferentes cenários com base no tipo de conta selecionado (conta_normal, conta_universitaria e conta_especial). Dependendo do tipo de conta, ele verifica o saldo disponível, o valor de saque e o limite de cheque especial para determinar se o saque é possível. Em seguida, ele imprime mensagens apropriadas com base nas condições verificadas. Se nenhum tipo de conta for reconhecido, ele indica que o sistema não reconheceu o tipo de conta e instrui a entrar em contato com o gerente.