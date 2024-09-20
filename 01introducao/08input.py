# input() para receber dados do usuario
# para executar: cmd py 08input.py
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

# format 1
print("1 - Nome {0} e possui {1} anos".format(nome, idade))

# format 2
print(f"2 - Nome {nome} e possui {idade} anos")

# exercicio
print("Calculo de area de retangulo")
base = input("Base do retangulo: ")
altura = input("Altura do retangulo: ")
area = float(base) * float(altura)
print(f"3 - Area do retangulo e {area} unidades!")
