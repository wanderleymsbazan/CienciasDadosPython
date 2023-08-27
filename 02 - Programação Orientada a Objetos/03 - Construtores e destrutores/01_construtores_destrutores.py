class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()

# Neste código, uma classe Cachorro é definida com um construtor para inicializar suas propriedades, um método destrutor para ser chamado quando uma instância é removida e um método falar para o cachorro emitir um som. Uma função criar_cachorro é criada para criar um cachorro chamado "Zeus" e exibir seu nome. Em seguida, uma instância chamada "c" é criada da classe Cachorro com nome "Chappie" e cor "amarelo", e o método falar é chamado para essa instância. Depois, a instância "c" é removida explicitamente, e mensagens são exibidas múltiplas vezes. A última linha que chama a função criar_cachorro está comentada e não será executada.