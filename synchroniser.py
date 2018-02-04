import os
import sys
import shutil
import time
from distutils.dir_util import copy_tree
argument=sys.argv[1:]
def synchro(src,dest):
        liste_fichier_src=os.listdir(src)
        liste_fichier_dest=os.listdir(dest)
        nb_fichier=len(liste_fichier_src)
        for i in range(0,nb_fichier):
            if os.path.isfile(os.path.join(src,liste_fichier_src[i])):
                if not(liste_fichier_src[i]in liste_fichier_dest):
                    shutil.copy(os.path.join(src,liste_fichier_src[i]),dest)
                else:
                    if os.path.getmtime(os.path.join(src,liste_fichier_src[i]))>os.path.getmtime(os.path.join(dest,liste_fichier_src[i])):
                        shutil.copy(os.path.join(src,liste_fichier_src[i]),dest)
            else :
                if not(liste_fichier_src[i]in liste_fichier_dest):
                    copy_tree(os.path.join(src,liste_fichier_src[i]),os.path.join(dest,liste_fichier_src[i]))
                else:
                    synchro(os.path.join(src,liste_fichier_src[i]),os.path.join(dest,liste_fichier_src[i]))
        return
def synchro_teste(src,dest):
        liste_fichier_src=os.listdir(src)
        liste_fichier_dest=os.listdir(dest)
        nb_fichier=len(liste_fichier_src)
        for i in range(0,nb_fichier):
            if os.path.isfile(os.path.join(src,liste_fichier_src[i])):
                if not(liste_fichier_src[i]in liste_fichier_dest):
                    print('copie du fichier '+liste_fichier_src[i])
                else:
                    if os.path.getmtime(os.path.join(src,liste_fichier_src[i]))>os.path.getmtime(os.path.join(dest,liste_fichier_src[i])):
                        print('mise a jour du fichier '+liste_fichier_src[i])
            else :
                if not(liste_fichier_src[i]in liste_fichier_dest):
                    print('copie du dossier '+liste_fichier_src[i])
                else:
                    synchro_teste(os.path.join(src,liste_fichier_src[i]),os.path.join(dest,liste_fichier_src[i]))
        return
  

if len(argument)==2:
    src=argument[0]
    dest=argument[1]
    synchro_teste(src,dest)
elif len(argument)==3 and argument[0]=='-f':
    src=argument[1]
    dest=argument[2]
    synchro(src,dest)
               
    
