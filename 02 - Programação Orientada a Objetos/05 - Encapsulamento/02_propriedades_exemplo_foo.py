# Definição da classe Foo
class Foo:
    # Método construtor da classe Foo, com o argumento opcional x (padrão é None)
    def __init__(self, x=None):
        self._x = x  # Atributo _x (privado) recebe o valor x informado no construtor

    # Propriedade (getter) x para acessar o valor do atributo _x
    @property
    def x(self):
        return self._x or 0  # Retorna o valor de _x, se existir; caso contrário, retorna 0

    # Setter da propriedade x para modificar o valor do atributo _x
    @x.setter
    def x(self, value):
        self._x += value  # Incrementa o valor de _x com o valor informado

    # Deleter da propriedade x para remover o valor do atributo _x
    @x.deleter
    def x(self):
        self._x = 0  # Atribui 0 ao atributo _x para "deletar" seu valor

# Criação de uma instância da classe Foo com o valor inicial x=10
foo = Foo(10)

print(foo.x)  # Imprime o valor de x, que é 10 (definido no construtor)
del foo.x  # Remove o valor de x da instância
print(foo.x)  # Imprime o valor de x, que é 0 (getter x retorna 0 quando _x é None)
foo.x = 10  # Define o valor de x na instância para 10
print(foo.x)  # Imprime o valor de x, que é 20 (incrementado com o valor 10)

#Estes comentários explicam como a classe Foo define uma propriedade x com getter, setter e deleter, demonstrando como a propriedade é utilizada para acessar e modificar o valor do atributo _x de maneira controlada.