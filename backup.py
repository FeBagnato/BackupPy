import os

dirHome = str(os.environ['HOME'])

def backupStart(pasta):
   os.chdir("{}/{}/".format(dirHome,pasta))
   os.mkdir("./Backup {}".format(pasta))
   print("Copiando os itens de {}".format(pasta))
   for iten in os.listdir():
      if iten.replace(' ',"\ ") == "Backup\ {}".format(pasta):
         print('')
      else:
         os.system("cp -rf {} Backup\ {}".format(iten.replace(' ', "\ "),pasta))
         print("Copiando {}".format(iten.replace(' ','\ ')))
   os.system('notify-send -i gtk-dialog-warning -u normal "Backup" "Digite a sua senha"')
   os.system("7z a -p Backup\ {}.7z Backup\ {}".format(pasta,pasta))
   os.system("tar -cvf Backup\ {}.7z.tar Backup\ {}.7z".format(pasta,pasta))

   os.system("rm -dr Backup\ {}".format(pasta))
   os.system("rm Backup\ {}.7z".format(pasta))


backupStart("Documentos")

backupStart("Downloads")

backupStart("Desktop")

backupStart("Imagens")

backupStart("Música")

backupStart("Vídeos")
