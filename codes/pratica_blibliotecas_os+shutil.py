import os
import shutil

caminho_original = input('Digite o caminho original: ')  # exemplo: r'D:\Vini\Pictures\imgxD'
caminho_novo = input('Digite o caminho novo: ')  # exemplo r'D:\Vini\Pictures\imgxD2'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        new_path_file = os.path.join(caminho_novo, file)
        old_path_file = os.path.join(root, file)
        nome_arq, ext_arq = os.path.splitext(file)

        if ext_arq == '.jpg':
            shutil.copy(old_path_file, new_path_file)
            print(f'Arquivo {file} copiado para a nova pasta {new_path_file}')  # fazendo copia de arquivos

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        new_path_file2 = os.path.join(root, file)
        nome_arq, ext_arq = os.path.splitext(file)

        if ext_arq == '.jpg':
            os.remove(new_path_file2)
            print(f'Arquivo {file} excluído da pasta {new_path_file2}')  # excluíndo arquivos
