# Definição da classe Conta
class Conta:
    # Método construtor da classe Conta, recebe o número da agência e um saldo opcional (padrão é 0)
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo  # Atributo _saldo (privado) recebe o saldo informado no construtor
        self.nro_agencia = nro_agencia  # Atributo nro_agencia recebe o número da agência informado

    # Método para realizar um depósito na conta
    def depositar(self, valor):
        self._saldo += valor  # Incrementa o valor ao saldo

    # Método para realizar um saque na conta
    def sacar(self, valor):
        self._saldo -= valor  # Decrementa o valor do saldo

    # Método para mostrar o saldo atual da conta
    def mostrar_saldo(self):
        return self._saldo  # Retorna o saldo atual

# Criação de uma instância da classe Conta com o número da agência "0001" e saldo inicial de 100
conta = Conta("0001", 100)
conta.depositar(100)  # Realiza um depósito de 100 na conta

print(conta.nro_agencia)  # Imprime o número da agência da conta
print(conta.mostrar_saldo())  # Imprime o saldo atual da conta
