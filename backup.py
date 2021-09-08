import os
import py7zr
from getpass import getpass
from shutil import rmtree

dirHome = str(os.environ['HOME'])


def backupStart(pasta):
    os.chdir("{}/{}/".format(dirHome, pasta))
    os.mkdir("./Backup {}".format(pasta))
    print("Copiando os itens de {}".format(pasta))
    for iten in os.listdir():
        if iten.replace(' ', "\ ") == "Backup\ {}".format(pasta):
            print('')
        else:
            os.system("cp -rf {} Backup\ {}".format(iten.replace(' ', "\ "),pasta))
            print("\033[97mCopiando \033[32m{}".format(iten.replace(' ', '\ ')))
    print('\033[97m')

    with py7zr.SevenZipFile("Backup {}.7z".format(pasta), 'w', password=senha) as backup:
        backup.writeall("Backup {}/".format(pasta))
    rmtree("Backup {}".format(pasta))


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
