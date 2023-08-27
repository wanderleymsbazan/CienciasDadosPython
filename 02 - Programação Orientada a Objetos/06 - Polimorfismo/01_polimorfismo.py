# Definição da classe Passaro
class Passaro:
    # Método voar da classe base, que pode ser sobrescrito pelas subclasses
    def voar(self):
        print("Voando...")

# Definição da classe Pardal, que herda da classe Passaro
class Pardal(Passaro):
    # Sobrescrita do método voar da classe base
    def voar(self):
        print("Pardal pode voar")

# Definição da classe Avestruz, que herda da classe Passaro
class Avestruz(Passaro):
    # Sobrescrita do método voar da classe base
    def voar(self):
        print("Avestruz não pode voar")

# Definição da classe Aviao, que "herda" da classe Passaro (não é uma herança adequada)
class Aviao(Passaro):
    # Sobrescrita do método voar da classe base
    def voar(self):
        print("Avião está decolando...")

# Função plano_voo que recebe um objeto e chama o método voar do objeto
def plano_voo(obj):
    obj.voar()

# Criando instâncias das classes Pardal, Avestruz e Aviao e chamando a função plano_voo para cada uma delas
plano_voo(Pardal())  # O método voar da classe Pardal é chamado
plano_voo(Avestruz())  # O método voar da classe Avestruz é chamado
plano_voo(Aviao())  # O método voar da classe Aviao é chamado

# Estes comentários explicam como as classes Passaro, Pardal, Avestruz e Aviao são definidas, mostrando como as subclasses podem sobrescrever o método voar da classe base. No final, a função plano_voo é usada para demonstrar o uso das diferentes subclasses, com foco especial na classe Aviao, que não deveria herdar de Passaro.