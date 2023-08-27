# Definição da classe base Animal
class Animal:
    # Método construtor da classe Animal
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas  # Atributo nro_patas recebe o valor passado como argumento

    # Método especial para exibir informações do animal em formato de string
    def __str__(self):
        # Criação da representação em string do objeto com seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Definição da classe Mamifero, que herda da classe Animal
class Mamifero(Animal):
    # Método construtor da classe Mamifero
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo  # Atributo cor_pelo recebe o valor passado como argumento
        super().__init__(**kw)  # Chama o construtor da classe base (Animal)

# Definição da classe Ave, que herda da classe Animal
class Ave(Animal):
    # Método construtor da classe Ave
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico  # Atributo cor_bico recebe o valor passado como argumento
        super().__init__(**kw)  # Chama o construtor da classe base (Animal)

# Definição da classe Gato, que herda da classe Mamifero
class Gato(Mamifero):
    pass  # Classe Gato não possui métodos ou atributos adicionais

# Definição da classe Ornitorrinco, que herda das classes Mamifero e Ave
class Ornitorrinco(Mamifero, Ave):
    # Método construtor da classe Ornitorrinco
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # Chama o construtor da classe base Mamifero e Ave com os argumentos correspondentes
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

# Criação de uma instância da classe Gato
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

# Criação de uma instância da classe Ornitorrinco
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
