import sqlite3

master_pass = '12345'

acess_primary = input('Digite a senha: ')
if acess_primary != master_pass:
    print('Acesso negado!')
    exit()

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE if not exists users (
        tipo TEXT NOT NULL,
        usuario TEXT NOT NULL,
        password TEXT NOT NULL);    
''')


def menu():
    print('*' * 35)
    print('Selecione uma opção')
    print('1: Inserir nova senha')
    print('2: Lista de plataformas')
    print('3: Senha de plataforma específica')
    print('4: Todas as senhas')
    print('5: Sair')
    print('*' * 35)


def ins_password():
    try:
        tipo = input('Digite a plataforma: ')
        user = input('Digite o user: ')
        passw = input('Digite a senha: ')
        cursor.execute(f"""
            INSERT INTO users(tipo, usuario, password)
            VALUES ('{tipo}', '{user}', '{passw}')
            """)
        conn.commit()
    except sqlite3.Error as erro:
        print(f'Ocorreu o seguinte erro: {erro}')
    else:
        print('Registro realizado')


def list_serv():
    cursor.execute('SELECT tipo from users;')
    print('Plataformas: ')
    for tipos in cursor.fetchall():
        print(tipos)


def password_espec():
    try:
        tipoesc = input('Digite a plataforma que deseja consultar: ')
        cursor.execute(f"""SELECT usuario, password from users
                            WHERE tipo = '{tipoesc}'
                       """)
        if cursor.rowcount == 0:
            print('Serviço não cadastrado, utilize a opção 2 para consultar as plataformas')
        else:
            for types in cursor.fetchall():
                print(types)
    except conn.Error as erro:
        print(f'Ocorreu o seguinte erro: {erro}')


def all_passwords():
    cursor.execute('SELECT * FROM users;')
    for tudo in cursor.fetchall():
        print(f'Plataforma: {tudo[0]}')
        print(f'Usuario: {tudo[1]}')
        print(f'Senha: {tudo[2]}')
        print('*' * 15)


def close_all():
    cursor.close()
    conn.close()


op = True
if __name__ == '__main__':
    opcoes = [ins_password, list_serv, password_espec, all_passwords]
    while True:
        if op:
            menu()
            op = False
        try:
            escolha = int(input('Digite uma opção: '))
            if escolha == 5:
                close_all()
                break
            elif escolha == 0:
                raise ValueError('O valor não pode ser 0')
            else:
                opcoes[escolha - 1]()
                op = True
        except (ValueError, IndexError):
            print('Digite um opção válida')

print('Encerrando sistema!')
