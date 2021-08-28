import requests

try:
    print('Digite seu CEP: ', end='')
    get_cep = str(input()).strip()

    for num in get_cep:
        if num == '-' or '.':
            num.replace(num, '')

    r = requests.get(f'https://viacep.com.br/ws/{get_cep}/json/')
    r = r.json()

    for chave, valor in r.items():
        print(chave, ':', valor)
except Exception as erro:
    print(f'CEP inválido, erro: {erro}')
