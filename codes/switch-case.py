def choice():
    a = int(input('N1: '))
    b = int(input('N2: '))
    return a , b

def soma():
    z, y = choice()
    return z + y


def sub():
    z, y = choice()
    return z - y


def mult():
    z, y = choice()
    return z * y


def div():
    z, y = choice()
    return f"{z / y:.2f}"


def invalid():
    return 'Opção inválida'

print("""
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
""")
escolha = int(input('Escolha a operação: '))

# Opção com listas
# operations = [soma, sub, mult, div]
# output = operations[escolha - 1]()
# print(output)

# Opção com dicionario
operations = {
    1: soma,
    2: sub,
    3: mult,
    4: div
}
output = operations.get(escolha, invalid)()
print(output)
