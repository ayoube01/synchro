#not finished yet
import os
import sys
def CountOccurencesInText(word,text):
    compteur=0
    new_liste=[]
    last_liste=[]
    last_new_liste=[]
    liste=text.split("\n")
    for element in liste:
        a=element.split(" ")
        for z in a:
            new_liste.append(z)
    for mot in new_liste :
        for i in mot:
            if  (ord(i)>94 and ord(i)<124)or (ord(i)<91 and ord(i)>64):
                mot=mot
            else:
                mot=mot.replace(i,'')
        last_new_liste.append(mot)
    for mot in last_new_liste:
        if mot.upper()==word.upper():
            compteur+=1
    return compteur


print(CountOccurencesInText("python","""Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""))
