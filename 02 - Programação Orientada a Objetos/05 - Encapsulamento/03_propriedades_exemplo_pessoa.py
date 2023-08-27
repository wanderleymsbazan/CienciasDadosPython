# Definição da classe Pessoa
class Pessoa:
    # Método construtor da classe Pessoa, com argumentos nome e ano_nascimento
    def __init__(self, nome, ano_nascimento):
        self.nome = nome  # Atributo nome recebe o valor do argumento nome
        self._ano_nascimento = ano_nascimento  # Atributo _ano_nascimento recebe o valor do argumento ano_nascimento

    # Propriedade (getter) idade para calcular e retornar a idade da pessoa
    @property
    def idade(self):
        _ano_atual = 2023  # Ano atual usado para calcular a idade
        return _ano_atual - self._ano_nascimento  # Retorna a idade calculada

# Criação de uma instância da classe Pessoa com o nome "Wanderley" e ano de nascimento 1994
pessoa = Pessoa("Wanderley", 1982)

# Imprime o nome da pessoa e sua idade calculada usando a propriedade idade
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# Estes comentários explicam como a classe Pessoa define uma propriedade idade que utiliza o ano de nascimento para calcular a idade atual da pessoa com base no ano atual (2023). Em seguida, o código cria uma instância da classe e imprime o nome da pessoa e sua idade calculada.