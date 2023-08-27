class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Cria uma instância da classe Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Chama os métodos da instância
b1.buzinar()
b1.correr()
b1.parar()

# Acessa os atributos da instância diretamente
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Cria outra instância da classe Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)

# Imprime a representação da instância usando o método __str__
print(b2)

# Chama o método correr na instância b2
b2.correr()

#     Bicicleta é uma classe que tem um construtor __init__ para inicializar seus atributos (cor, modelo, ano e valor). Ela também tem métodos como buzinar, parar e correr.

#     A função especial __str__ é definida para personalizar a representação em string da instância da classe.

#     Duas instâncias b1 e b2 da classe Bicicleta são criadas com diferentes valores de atributos.

#     Métodos como buzinar, correr e parar são chamados nas instâncias b1 e b2.

#     Os atributos da instância b1 são acessados diretamente para imprimir informações.

#     A instância b2 é impressa usando o método __str__.

# Esse código demonstra como definir uma classe em Python, criar instâncias dessa classe e trabalhar com seus métodos e atributos.