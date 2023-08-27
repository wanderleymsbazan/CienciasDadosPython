def sacar(valor):
    saldo = 500  # Define o saldo inicial como 500.

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500  # Define o saldo inicial como 500.
    saldo += valor  # Aumenta o saldo com o valor depositado.

sacar(1000)  # Chama a função sacar com um valor de 1000.

#Nesse código, há duas funções definidas: sacar(valor) e depositar(valor). Aqui está o que cada função faz:

#     A função sacar(valor):
#         Define um saldo inicial de 500.
#         Verifica se o saldo é maior ou igual ao valor solicitado para saque.
#         Se a condição for verdadeira, imprime mensagens de "Valor sacado!" e instruções para retirar o dinheiro.
#         Independentemente do saldo, imprime a mensagem "Obrigado por ser nosso cliente, tenha um bom dia!"

#     A função depositar(valor):
#         Define um saldo inicial de 500.
#         No entanto, ela apenas aumenta o valor da variável saldo em valor, não atualizando o saldo real.

# A linha sacar(1000) chama a função sacar com um valor de 1000. No entanto, o saldo sempre é 500 dentro das funções, e elas não modificam o saldo real fora do escopo das funções. Portanto, ao executar o código como está, apenas as mensagens da função sacar serão impressas, mas o saldo não será afetado.

# A identação é um conceito fundamental na programação que se refere ao recuo ou espaçamento utilizado para estruturar visualmente o código fonte. Ela é usada para definir blocos de código, como loops, condicionais, funções e classes, indicando quais linhas de código estão contidas dentro de determinada estrutura.

# Em muitas linguagens de programação, incluindo Python, a identação não é apenas uma questão de estilo de codificação, mas é parte da sintaxe da linguagem. Em Python, a identação correta é obrigatória para que o código funcione corretamente. Isso significa que a organização do código em blocos é feita através do recuo das linhas, em vez de usar chaves ou palavras-chave especiais para delimitar blocos de código, como é comum em outras linguagens.

# Aqui estão alguns pontos-chave sobre identação:

#     Delimitação de Blocos: Em Python, a identação é usada para delimitar blocos de código, como loops (for e while), condicionais (if, else, elif), funções e classes. O bloco é composto pelas linhas de código com o mesmo recuo.

#     Consistência: A identação consistente torna o código mais legível e compreensível. É importante manter a mesma quantidade de espaços ou tabulações para todos os níveis de recuo.

#     Espaços ou Tabulações: Embora ambos possam ser usados para identação, é uma prática recomendada utilizar espaços em vez de tabulações. O uso consistente de espaços evita problemas de formatação quando o código é visualizado em diferentes ambientes.

#     Erros de Indentação: Erros de identação são comuns, especialmente para programadores iniciantes em Python. Indentação inadequada pode levar a erros de sintaxe e comportamento inesperado no código.

#     Níveis de Indentação: Cada nível de estrutura deve ser recuado por um número fixo de espaços (geralmente 4 espaços) ou tabulações. Isso cria uma hierarquia visual no código.

#     Finalização de Blocos: Em Python, o fim de um bloco é indicado pela diminuição do recuo para o nível anterior.

# Exemplo de identação em Python:

# python

for i in range(5):
    if i % 2 == 0:
        print("Número par:", i)
    else:
        print("Número ímpar:", i)
print("Fim do loop")

# Observe como a identação define claramente os blocos do loop for e do condicional if-else. Isso torna o código mais legível e ajuda a entender a estrutura lógica do programa.

# Em resumo, a identação é uma parte fundamental da sintaxe do Python e desempenha um papel crucial na legibilidade e estruturação do código. É importante seguir as convenções de identação e manter uma formatação consistente para garantir que o código seja fácil de entender e manter.
