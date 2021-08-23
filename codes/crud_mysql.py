import mysql.connector
from mysql.connector import Error


def pulalinha():
    print('-=' * 30)


def menu():
    print()
    pulalinha()
    print('Quadro de opções MySQL'.center(60))
    pulalinha()
    print("""
        1. Adicionar novo registro
        2. Editar quantidade ou preço de registro existente
        3. Nova consulta ao banco de dados
        4. Finalizar sessão
        """)
    pulalinha()


def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost', database='estudos', user='root', password='')
    except Error as erro:
        print(f'Houve um erro ao tentar se conectar ao MySQL: {erro}')


def createcursor(consultas=None):
    global cursor
    cursor = con.cursor()
    if consultas is not None:
        cursor.execute(consultas)


def desconectar():
    if con.is_connected():
        cursor.close()
        con.close()
        print('MySQL e cursor finalizados.')


def consulta():
    try:
        conectar()
        consulta_sql = 'select * from produtos'
        createcursor(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f'IdProduto: {linha[0]}')
            print(f'Nome: {linha[1]}')
            print(f'Preço: {linha[2]}')
            print(f'Quantidade: {linha[3]}')
            pulalinha()
    except Error as erro:
        print(f'Erro na consulta: {erro}')


def addRegistro():
    try:
        conectar()
        nomeprod = input('Nome do produto: ')
        precoprod = input('Preço: ')
        quantprod = input('Quantidade: ')
        consulta_sql = f"""insert into produtos(desc_produtos, preco_produtos, quantidade_produtos) values
                            ('{nomeprod}', '{precoprod}', '{quantprod}') """
        createcursor(consulta_sql)
        con.commit()
        print('Novo registro adicionado!')
    except Error as erro:
        print(f'Erro ao adicionar registro: {erro}')


def opsregistros():
    print('Qual produto deseja editar ')
    indice = int(input('Index: '))
    colunaup = int(input('[1]Preço \n[2]Quantidade \nOp: '))
    if colunaup == 1:
        novopreco = input('Novo preço: ')
        return updateregistro(indice, colunaup, novopreco)
    elif colunaup == 2:
        novaquant = input('Nova quantidade: ')
        return updateregistro(indice, colunaup, novaquant)


def updateregistro(index, column, novodado):
    try:
        conectar()
        if column == 1:
            declar = f"""UPDATE produtos set preco_produtos = {novodado} where id_produtos = {index}"""
            createcursor(declar)
            print('Preço Atualizado!')
        elif column == 2:
            declar2 = f"""UPDATE produtos set quantidade_produtos = {novodado} where id_produtos = {index}"""
            createcursor(declar2)
            print('Quantidade Atualizada!')
        con.commit()
    except Error as erro:
        print(f'Erro ao editar registro: {erro}')


def finish():
    return 'Finalizando sessão!'


if __name__ == '__main__':
    while True:
        resposta = ' '
        menu()
        while True:
            try:
                escolha = int(input('Opção: '))
                opcoes = [addRegistro, opsregistros, consulta, finish]
                output = opcoes[escolha - 1]()
            except (ValueError, TypeError):
                print('ERRO: use um número inteiro válido, digite novamente')
                continue
            except IndexError:
                print('ERRO: Número fora da lista, digite novamente')
            else:
                break
        if escolha == 4:
            print(output)
            desconectar()
            break
        pulalinha()
        while resposta not in 'SN':
            resposta = str(input('Deseja voltar ao menu? [S/N]: ')).upper().strip()[0]
        if resposta == 'N':
            print(finish())
            desconectar()
            break
