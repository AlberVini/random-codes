from random import randint, choice, shuffle


def zero_nove():
    return chr(randint(48, 57))


def a_z_minusc():
    return chr(randint(97, 122))


def a_z_maiusc():
    return chr(randint(65, 90))


def caracteres_especiais():
    rand_range = [
        randint(33, 47),
        randint(58, 64)
    ]

    return chr(choice(rand_range))


def create_senha(
    length=12,
    number=True,
    upper=True,
    lower=True,
    chars=2
):
    password = []

    especial = True
    while len(password) < length:
        if especial and chars > 0:
            especial = False
            for c in range(chars):
                password.append(caracteres_especiais())
        if upper:
            password.append(a_z_maiusc())
        if lower:
            password.append(a_z_minusc())
        if number:
            password.append(zero_nove())
        
    password = password[:length]
    shuffle(password)
    return ''.join(password)


def opcoes_senha():
    qnt_senhas = int(input('Quantidade de senhas geradas: '))
    digitos = int(input('Senha de quantos dígitos: '))
    caracteres_esp = int(input('Quantos caracteres especiais deseja na senha: '))
    return qnt_senhas, digitos, caracteres_esp


def principal():

    lista_senhas = list()

    qnt_senhas, digitos, caracteres_esp = opcoes_senha()

    # DEFAULT
    for c in range(qnt_senhas):
        lista_senhas.append(create_senha(
            length= digitos,
            chars= caracteres_esp
        ))

    # SEM MAIUSCULAS
    for c in range(qnt_senhas):
        lista_senhas.append(create_senha(
            length= digitos,
            chars= caracteres_esp,
            upper= False
        ))

    # SEM MINUSCULAS
    for c in range(qnt_senhas):
        lista_senhas.append(create_senha(
            length= digitos,
            chars = caracteres_esp,
            lower= False,
        ))

    # SÓ NÚMEROS
    for c in range(qnt_senhas):
        lista_senhas.append(create_senha(
            length= digitos,
            chars = 0,
            lower= False,
            upper= False
        ))

    return qnt_senhas, lista_senhas


def exib_senhas():
    qnt_password, ls = principal()
    
    print()
    print('SENHAS FORTES')
    for qnt in ls[:qnt_password]:
        print(qnt)
    print()

    print('SEM MAIUSCULAS')
    for qnt in ls[qnt_password:qnt_password*2]:
        print(qnt)
    print()

    print('SEM MINUSCULAS')
    for qnt in ls[qnt_password*2:qnt_password*3]:
        print(qnt)
    print()

    print('SOMENTE NÚMEROS')
    for qnt in ls[qnt_password*3:]:
        print(qnt)
    print()


if __name__ == "__main__":
    exib_senhas()
