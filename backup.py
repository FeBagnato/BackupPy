import os
import py7zr
from shutil import rmtree

dirHome = str(os.environ['HOME'])

def backupStart(pasta):
    passError = True
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
    os.system('notify-send -i gtk-dialog-warning -u normal "Backup" "Digite a sua senha"')

    while(passError):
        senha = str(input("Digite a senha: "))

        if(senha == str(input("Digite a senha novamente: "))):
            with py7zr.SevenZipFile("Backup {}.7z".format(pasta), 'w', password=senha) as backup:
                backup.writeall("Backup {}/".format(pasta))
            passError = False
        else:
            print("\033[0;31mA senha esta incorreta!")
            print("Tente novamente\n\033[97m")

    rmtree("Backup {}".format(pasta))


backupStart("Documentos")

backupStart("Downloads")

backupStart("Desktop")

backupStart("Imagens")

backupStart("Música")

backupStart("Vídeos")
