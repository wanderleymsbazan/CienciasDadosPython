MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))  # Solicita ao usuário que informe sua idade.

# Verifica se a idade é maior ou igual à idade de maioridade.
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

# Verifica se a idade é menor que a idade de maioridade.
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

#Nesse trecho do código, há uma verificação direta da idade em relação à maioridade. Se a idade for maior ou igual à idade definida como MAIOR_IDADE, o programa informa que a pessoa pode tirar a Carteira Nacional de Habilitação (CNH). Se a idade for menor que a maioridade, o programa informa que a pessoa ainda não pode tirar a CNH.

# Verifica se a idade é maior ou igual à idade de maioridade.
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")

#Nessa parte, o mesmo teste é realizado, mas desta vez é utilizado um else, que cobre o caso em que a idade não atinge a maioridade. Se a idade for maior ou igual à MAIOR_IDADE, a mensagem sobre a CNH é impressa. Caso contrário, a mensagem de que ainda não é possível tirar a CNH é impressa.

# Verifica se a idade é maior ou igual à idade de maioridade.
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
# Verifica se a idade é igual à idade especial.
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

#Aqui, o programa verifica se a idade é maior ou igual à maioridade. Se sim, informa que a pessoa pode tirar a CNH. Caso contrário, verifica se a idade é igual à IDADE_ESPECIAL. Se for, a mensagem indica que a pessoa pode fazer aulas teóricas, mas não práticas. Se a idade não atender a nenhuma dessas condições, a mensagem sobre não poder tirar a CNH é impressa.