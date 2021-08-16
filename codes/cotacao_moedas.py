import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL") # BTC-BRL
cotacoes = cotacoes.json()

for moeda, inf in cotacoes.items():
    print(f'Moeda: {moeda}')
    for tipo, valor in inf.items():
        if tipo == 'high':
            valor = float(valor)
            print('Maior variação do dia: R${:.2f}'.format(valor))
        if tipo == 'low':
            valor = float(valor)
            print('Menor variação do dia: R${:.2f}'.format(valor)) 
        if tipo == 'bid':
            valor = float(valor)
            print('Cotação atual: R${:.2f}'.format(valor))
    print('-' * 35)
