while True:
    try:
        a = int(input('A: '))
        b = int(input('B: '))
        c = int(input('C: '))
    except ValueError:
        print('Valor(es) inválidos.')
    else:
        delta = (b ** 2) - (4 * a * c)
        sol1 = (-b - delta**(1/2)) / (2 * a)
        sol2 = (-b + delta**(1/2)) / (2 * a)
        print(f'Resultados {sol1:.2f} e {sol2:.2f}')
        break
