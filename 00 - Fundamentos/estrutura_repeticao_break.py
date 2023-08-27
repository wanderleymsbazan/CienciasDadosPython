# Um loop infinito que continuará pedindo números ao usuário até que o loop seja interrompido.
while True:
    numero = int(input("Informe um número: "))  # Solicita ao usuário que insira um número.

    if numero == 10:
        break  # Se o número inserido for 10, o loop é interrompido.

    if numero % 2 == 0:
        continue  # Se o número for par, o loop continua para a próxima iteração.

    print(numero)  # Se o número for ímpar (diferente de 10), ele é impresso.



# Um loop que itera sobre uma sequência de números de 0 a 99.
for numero in range(100):
    if numero % 2 == 0:
        continue  # Se o número for par, o loop continua para a próxima iteração.

    print(numero, end=" ")  # Se o número for ímpar, ele é impresso, separado por espaço.

#Esse código utiliza os conceitos de loops (while e for) e as instruções break e continue para controlar o fluxo de execução. Ele solicita ao usuário números inteiros e, caso o número seja 10, o loop é encerrado. Se o número for ímpar, ele é impresso. O trecho comentado com o loop for realiza uma tarefa semelhante, imprimindo números ímpares de 0 a 99.