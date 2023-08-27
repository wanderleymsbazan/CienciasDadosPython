# Definição da classe Pessoa
class Pessoa:
    # Construtor da classe Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de classe que cria uma instância da classe a partir da data de nascimento
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # Calculando a idade com base no ano de nascimento fornecido
        idade = 2023 - ano
        # Criando e retornando uma instância da classe com os valores fornecidos
        return cls(nome, idade)

    # Método estático que verifica se uma pessoa é maior de idade com base na idade fornecida
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# Criando uma instância da classe Pessoa usando o método de classe criar_de_data_nascimento
p = Pessoa.criar_de_data_nascimento(1982, 2, 16, "Wanderley")
print(p.nome, p.idade)

# Chamando o método estático e_maior_idade para verificar se uma idade é maior de 18
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

# Os comentários explicam como a classe Pessoa é definida, com um construtor e dois métodos especiais. O método de classe criar_de_data_nascimento permite criar uma instância da classe com base na data de nascimento fornecida. O método estático e_maior_idade verifica se uma pessoa é maior de idade com base na idade fornecida. O código também demonstra como usar esses métodos para criar instâncias e fazer verificações.