# Definição da classe base Veiculo
class Veiculo:
    # Método construtor da classe Veiculo
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor  # Atributo cor recebe o valor passado como argumento
        self.placa = placa  # Atributo placa recebe o valor passado como argumento
        self.numero_rodas = numero_rodas  # Atributo numero_rodas recebe o valor passado como argumento

    # Método para ligar o motor do veículo
    def ligar_motor(self):
        print("Ligando o motor")

    # Método especial para exibir informações do veículo em formato de string
    def __str__(self):
        # Criação da representação em string do objeto com seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Definição da classe Motocicleta, que herda da classe Veiculo
class Motocicleta(Veiculo):
    pass  # Classe Motocicleta não possui métodos ou atributos adicionais

# Definição da classe Carro, que herda da classe Veiculo
class Carro(Veiculo):
    pass  # Classe Carro não possui métodos ou atributos adicionais

# Definição da classe Caminhao, que herda da classe Veiculo
class Caminhao(Veiculo):
    # Método construtor da classe Caminhao
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # Chama o construtor da classe base (Veiculo)
        self.carregado = carregado  # Atributo carregado recebe o valor passado como argumento

    # Método para verificar se o caminhão está carregado
    def esta_carregado(self):
        # Imprime se o caminhão está carregado ou não baseado no valor do atributo carregado
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Criação de instâncias das classes Motocicleta, Carro e Caminhao
moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# Impressão das representações em string de cada instância
print(moto)
print(carro)
print(caminhao)
