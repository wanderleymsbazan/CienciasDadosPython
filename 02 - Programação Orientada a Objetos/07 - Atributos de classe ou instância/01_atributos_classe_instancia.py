# Definição da classe Estudante
class Estudante:
    # Atributo de classe, compartilhado por todas as instâncias da classe
    escola = "DIO"

    # Construtor da classe Estudante
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    # Método especial para retornar uma representação em string do objeto
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

# Função para mostrar os valores de uma lista de objetos
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Criando instâncias da classe Estudante
aluno_1 = Estudante("Wanderley", 1)
aluno_2 = Estudante("Giovanna", 2)

# Chamando a função mostrar_valores para mostrar as instâncias criadas
mostrar_valores(aluno_1, aluno_2)

# Modificando o atributo de classe "escola" para todos os objetos da classe Estudante
Estudante.escola = "Python"

# Criando uma nova instância da classe Estudante após a modificação do atributo de classe
aluno_3 = Estudante("Chappie", 3)

# Chamando a função mostrar_valores novamente para mostrar as instâncias atualizadas
mostrar_valores(aluno_1, aluno_2, aluno_3)

# Esses comentários explicam como a classe Estudante é definida, com atributos de classe e um construtor. A função mostrar_valores é utilizada para exibir os detalhes das instâncias da classe. O código também demonstra como um atributo de classe pode ser modificado e como essa mudança afeta as instâncias criadas posteriormente.