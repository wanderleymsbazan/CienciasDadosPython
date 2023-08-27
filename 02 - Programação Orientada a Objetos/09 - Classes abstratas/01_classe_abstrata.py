# Importando as classes ABC (Abstract Base Class), abstractmethod e abstractproperty do módulo abc
from abc import ABC, abstractmethod, abstractproperty

# Definindo a classe abstrata ControleRemoto que herda de ABC (Abstract Base Class)
class ControleRemoto(ABC):
    # Definindo o método abstrato ligar
    @abstractmethod
    def ligar(self):
        pass

    # Definindo o método abstrato desligar
    @abstractmethod
    def desligar(self):
        pass

    # Definindo a propriedade abstrata marca
    @property
    @abstractproperty
    def marca(self):
        pass

# Definindo a classe ControleTV que herda da classe ControleRemoto
class ControleTV(ControleRemoto):
    # Implementando o método ligar da classe ControleTV
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    # Implementando o método desligar da classe ControleTV
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    # Implementando a propriedade marca da classe ControleTV
    @property
    def marca(self):
        return "Philco"

# Definindo a classe ControleArCondicionado que herda da classe ControleRemoto
class ControleArCondicionado(ControleRemoto):
    # Implementando o método ligar da classe ControleArCondicionado
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    # Implementando o método desligar da classe ControleArCondicionado
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    # Implementando a propriedade marca da classe ControleArCondicionado
    @property
    def marca(self):
        return "LG"

# Criando uma instância da classe ControleTV
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

# Criando uma instância da classe ControleArCondicionado
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# Os comentários explicam a definição das classes abstratas ControleRemoto e as classes concretas ControleTV e ControleArCondicionado, bem como a implementação dos métodos abstratos e propriedades abstratas. Além disso, o código demonstra como criar instâncias das classes concretas e usar seus métodos e propriedades.