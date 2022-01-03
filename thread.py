import threading
import os
import py7zr
from shutil import rmtree

class BackupThread(threading.Thread):
    def __init__(self, pasta, senha):
        threading.Thread.__init__(self)
        self.pasta = pasta
        self.senha = senha
        self.dirHome = str(os.environ['HOME'])

    def run(self):
        os.chdir(f"{self.dirHome}/{self.pasta}/")
        os.mkdir(f"./Backup {self.pasta}")
        print(f"Copiando os itens de {self.self.pasta}")
        for iten in os.listdir():
            if iten.replace(' ', "\ ") == f"Backup\ {self.pasta}":
                print('')
            else:
                os.system(f"cp -rf '{iten}' Backup\ {self.pasta}")
                print(f"\033[97mCopiando \033[32m{iten}")
        print('\033[97m')

        with py7zr.SevenZipFile(f"Backup {self.pasta}.7z", 'w', password=self.senha) as backup:
            backup.writeall(f"Backup {self.pasta}/")
        rmtree(f"Backup {self.pasta}")