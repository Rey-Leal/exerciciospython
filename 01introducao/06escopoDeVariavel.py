# escopo de variaveis

# global
numeroGlobal = 5

# funcao


def somaMais(parametro):
    numero = 0  # local
    numero = numero + parametro
    print("Valor local: ", numero)


print("Valor global: ", numeroGlobal)

somaMais(2)
