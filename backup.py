import os
import py7zr
from getpass import getpass
from shutil import rmtree

dirHome = str(os.environ['HOME'])


def backupStart(pasta):
    os.chdir(f"{dirHome}/{pasta}/")
    os.mkdir(f"./Backup {pasta}")
    print(f"Copiando os itens de {pasta}")
    for iten in os.listdir():
        if iten.replace(' ', "\ ") == f"Backup\ {pasta}":
            print('')
        else:
            nomeIten = iten.replace(' ', "\ ")
            os.system(f"cp -rf {nomeIten} Backup\ {pasta}")
            print(f"\033[97mCopiando \033[32m{iten}")
    print('\033[97m')

    with py7zr.SevenZipFile(f"Backup {pasta}.7z", 'w', password=senha) as backup:
        backup.writeall(f"Backup {pasta}/")
    rmtree(f"Backup {pasta}")


passError = True
while(passError):
    senha = getpass("Digite a senha: ")

    if(senha == getpass("Digite a senha novamente: ")):
        backupStart("Documentos")
        backupStart("Downloads")
        backupStart("Desktop")
        backupStart("Imagens")
        backupStart("Música")
        backupStart("Vídeos")

        passError = False
    else:
        print("\033[0;31mA senha esta incorreta!")
        print("Tente novamente\n\033[97m")
