# Um menu com opções para depósito, saque, extrato e sair.
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Saldo inicial, limite de saque, registro do extrato, número de saques e limite máximo de saques.
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa, executa indefinidamente até a opção "q" (sair) ser escolhida.
while True:

    # Solicitação da escolha de opção do menu.
    opcao = input(menu)

    if opcao == "d":
        # Opção de depósito: solicita o valor a ser depositado.
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            # Se o valor for válido, atualiza o saldo e registra o depósito no extrato.
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        # Opção de saque: solicita o valor a ser sacado.
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o saque excede o saldo, o limite de saque e o limite de saques permitidos.
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            # Se todas as verificações passarem, atualiza o saldo, registra o saque no extrato e incrementa o número de saques.
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        # Opção de extrato: exibe o extrato e o saldo atual.
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        # Opção de sair: encerra o loop e finaliza o programa.
        break

    else:
        # Caso a opção escolhida seja inválida.
        print("Operação inválida, por favor selecione novamente a operação desejada.")

#Esse código é um exemplo de um programa simples que simula um sistema de controle de saldo bancário com opções de depósito, saque, exibição de extrato e sair. O programa utiliza condicionais para validar as operações, mantém registro do extrato e impõe limites de saque e quantidade de saques.