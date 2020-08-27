import os
from shutil import rmtree

dirHome = str(os.environ['HOME'])
varError = 1

def backupStart(pasta):
   os.chdir("{}/{}/".format(dirHome,pasta))
   os.mkdir("./Backup {}".format(pasta))
   print("Copiando os itens de {}".format(pasta))
   for iten in os.listdir():
      if iten.replace(' ',"\ ") == "Backup\ {}".format(pasta):
         print('')
      else:
         os.system("cp -rf {} Backup\ {}".format(iten.replace(' ', "\ "),pasta))
         print("\033[97mCopiando \033[32m{}".format(iten.replace(' ','\ ')))
   print('\033[97m')
   os.system('notify-send -i gtk-dialog-warning -u normal "Backup" "Digite a sua senha"')
   global varError
   while(varError != 0):
       varError = os.system("7z a -p Backup\ {}.7z Backup\ {}".format(pasta,pasta))
       if(varError != 0):
           print("\033[0;31mA senha digitada esta incorreta!")
           print("Tente novamente\033[97m")
   os.system("tar -cvf Backup\ {}.7z.tar Backup\ {}.7z".format(pasta,pasta))

   rmtree("Backup {}".format(pasta))
   os.remove("Backup {}.7z".format(pasta))


backupStart("Documentos")

backupStart("Downloads")

backupStart("Desktop")

backupStart("Imagens")

backupStart("Música")

backupStart("Vídeos")
