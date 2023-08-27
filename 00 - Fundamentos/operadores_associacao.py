frutas = ["limao", "uva"]
curso = "Curso de python"

# Verifica se "laranja" não está na lista de frutas.
print("laranja" not in frutas)

# Verifica se "limao" está na lista de frutas.
print("limao" in frutas)

# Verifica se "Python" está na string curso (diferença entre maiúsculas e minúsculas importa).
print("Python" in curso)

#     A lista frutas contém os elementos "limao" e "uva", e a variável curso contém a string "Curso de python".

#     A primeira linha print("laranja" not in frutas) verifica se a string "laranja" não está presente na lista frutas. Como "laranja" não está na lista, a expressão not in resulta em True, e isso é impresso na tela.

#     A segunda linha print("limao" in frutas) verifica se a string "limao" está presente na lista frutas. Como "limao" está na lista, a expressão in resulta em True, e isso é impresso na tela.

#     A terceira linha print("Python" in curso) verifica se a string "Python" está presente na string curso. No entanto, como as comparações em Python são sensíveis a maiúsculas e minúsculas, a expressão resulta em False, e isso é impresso na tela.

# O código demonstra como verificar a existência de elementos em listas e strings usando os operadores in e not in.