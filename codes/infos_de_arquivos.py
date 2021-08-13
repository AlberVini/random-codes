import os

caminho = str(input('Digite em que caminho deseja procurar: '))
termo = input('Digite algo especifico que quer procurar: ')


def formata_tamanho(tam):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tam < kilo:
        texto = 'B'
    elif tam < mega:
        tam /= kilo
        texto = 'K'
    elif tam < giga:
        tam /= mega
        texto = 'M'
    elif tam < tera:
        tam /= giga
        texto = 'G'
    elif tam < peta:
        tam /= tera
        texto = 'T'
    else:
        tam /= peta
        texto = 'P'

    tamanho1 = round(tam, 2)
    return f"{tamanho1}{texto}".replace('.', ',')


cont = 0
for raiz, diretorio, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                tamanho = os.path.getsize(caminho_completo)
                nome_arq, ext_arq = os.path.splitext(arquivo)
                print()
                print('Arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome do arquivo: ', nome_arq)
                print('Extensão do arquivo: ', ext_arq)
                print('Tamanho do arquivo: ', formata_tamanho(tamanho))
            except PermissionError:
                print('Sem permissão')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)

print()
print(f'{cont} arquivo(s) encontrado(s)')
