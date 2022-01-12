import thread
from getpass import getpass

print("""\033[0;33mCaso tenha algum arquivo ou pasta que você não queira adicionar ao backup, coloque o 
caminho no "ignoreList.conf" em "config/ignoreList.conf"\n""")

print("""Exemplo do conteúdo de ignoreList.conf:
/home/usuario/Downloads/ArquivoIgnorado\033[0;97m\n\n""")

passError = True
while(passError):
    senha = getpass("Digite a senha: ")

    if(senha == getpass("Digite a senha novamente: ")):
        backupDocumentos = thread.BackupThread("Documentos", senha)
        backupDownload = thread.BackupThread("Downloads", senha)
        backupDesktop = thread.BackupThread("Desktop", senha)
        backupImagens = thread.BackupThread("Imagens", senha)
        backupMusica = thread.BackupThread("Música", senha)
        backupVideos = thread.BackupThread("Vídeos", senha)

        backupDocumentos.start()
        backupDownload.start()
        backupDesktop.start()
        backupImagens.start()
        backupMusica.start()
        backupVideos.start()

        passError = False
    else:
        print("\033[0;31mA senha esta incorreta!")
        print("Tente novamente\n\033[97m")
