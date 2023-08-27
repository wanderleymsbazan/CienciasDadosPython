opcao = -1  # Inicializa a variável de opção com um valor diferente de 0.

# Enquanto a opção não for 0, o loop continua executando.
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n: "))  # Solicita ao usuário que escolha uma opção.

    if opcao == 1:
        print("Sacando...")  # Se a opção for 1, imprime "Sacando...".
    elif opcao == 2:
        print("Exibindo o extrato...")  # Se a opção for 2, imprime "Exibindo o extrato...".
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")  # Quando o loop termina, imprime uma mensagem de despedida.

#Nesse código, o programa entra em um loop while que continua a executar enquanto a opção inserida pelo usuário não for igual a 0. O programa exibe um menu de opções onde o usuário pode escolher entre sacar, exibir o extrato ou sair do sistema. Dependendo da opção escolhida, o programa exibe mensagens correspondentes. Quando o usuário escolhe a opção 0, o loop é interrompido e o programa exibe uma mensagem de despedida.