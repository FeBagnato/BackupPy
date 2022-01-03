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
        os.mkdir(f"{self.dirHome}/{self.pasta}/Backup {self.pasta}")
        print(f"Copiando os itens de {self.pasta}")
        for iten in os.listdir(f"{self.dirHome}/{self.pasta}"):
            if iten.replace(' ', "\ ") == f"Backup\ {self.pasta}":
                pass
            else:
                os.system(f"cp -rf '{self.dirHome}/{self.pasta}/{iten}' "
                          f"{self.dirHome}/{self.pasta}/Backup\ {self.pasta}")

                print(f"\033[97mCopiando \033[32m{iten}")
        print('\033[97m')

        with py7zr.SevenZipFile(f"{self.dirHome}/{self.pasta}/Backup {self.pasta}.7z", 'w',
                                password=self.senha) as backup:
            backup.writeall(f"{self.dirHome}/{self.pasta}/Backup {self.pasta}/",
                            f"Backup {self.pasta}")
        rmtree(f"{self.dirHome}/{self.pasta}/Backup {self.pasta}")
